import { createClient } from 'redis';

const client = createClient({
  url: 'redis://127.0.0.1:6379',
});


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

client.connect().catch((err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
