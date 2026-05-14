const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

// Load the parsed cargo JSON from Task 1
const cargoData = JSON.parse(fs.readFileSync('./cargo.json', 'utf-8'));

// GET /api/cargo
app.get('/api/cargo', (req, res) => {

  // Business Rule 3: Check for X-System-Override header
  if (req.headers['x-system-override'] === 'true') {
    return res
      .status(418)
      .type('text')
      .send('System override denied.');
  }

  // Normal response
  res.json(cargoData);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});