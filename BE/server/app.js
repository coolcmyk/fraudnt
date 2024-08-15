const express = require('express');
const alloydbService = require('./db/alloyDb');

const app = express();
app.use(express.json());

// Check if DATABASE_URI is set
if (!process.env.ALLOYDB_URI) {
  console.error('ALLOYDB_URI environment variable is not set');
  process.exit(1);
}

// Initialize AlloyDB connection
alloydbService.initializePool();

// Example API endpoint
app.get('/api/search', async (req, res) => {
  try {
    const { query } = req.query;
    // This is a simplified example. In a real application, you'd generate
    // the embedding for the query using an ML model.
    const queryEmbedding = [0.1, 0.2, 0.3]; // Example embedding

    const sql = `
      SELECT id, content, embedding <=> $1 AS distance
      FROM documents
      ORDER BY distance
      LIMIT 5;
    `;

    const result = await db.query(sql, [queryEmbedding]);
    res.json(result.rows);
  } catch (error) {
    console.error('Error in search:', error);
    res.status(500).json({ error: 'An error occurred during search' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});


// ... rest of your code
