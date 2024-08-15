const { AlloyDBAdminClient } = require('@google-cloud/alloydb');
const { Pool } = require('pg');

let pool;

async function initializePool() {
  const alloydbClient = new AlloyDBAdminClient();

  // Check if DATABASE_URI is set
  if (!process.env.ALLOYDB_URI) {
    throw new Error('DATABASE_URI environment variable is not set');
  }

  // Parse the URI to extract the instance path
  const uri = new URL(process.env.ALLOYDB_URI);
  const instancePath = uri.pathname.split('/').slice(1, -1).join('/');

  // Generate client certificate
  const [connectionInfo] = await alloydbClient.generateClientCertificate({
    parent: instancePath,
  });

  // Create pool using the DATABASE_URI
  pool = new Pool({
    connectionString: process.env.ALLOYDB_URI,
    ssl: {
      ca: connectionInfo.caCert,
      key: connectionInfo.clientKey,
      cert: connectionInfo.clientCert,
    },
  });

  // Test the connection
  try {
    await pool.query('SELECT NOW()');
    console.log('Successfully connected to AlloyDB');
  } catch (err) {
    console.error('Error connecting to AlloyDB:', err);
  }
}

async function query(text, params) {
  return pool.query(text, params);
}

module.exports = {
  initializePool,
  query,
};
