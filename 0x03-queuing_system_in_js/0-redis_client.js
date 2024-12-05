import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
