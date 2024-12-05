import { createClient } from 'redis';

// Create and configure the Redis client
const client = createClient({
  url: 'redis://127.0.0.1:6379',
});

// Event handlers for client connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Functions to interact with Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting key ${schoolName}: ${err.message}`);
    } else {
      console.log(reply); // Confirmation message
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving key ${schoolName}: ${err.message}`);
    } else {
      console.log(reply); // Log the value
    }
  });
}

// Ensure the client connects before performing operations
async function main() {
  try {
    await client.connect();

    // Perform operations
    displaySchoolValue('ALX');
    setNewSchool('ALXSanFrancisco', '100');
    displaySchoolValue('ALXSanFrancisco');
  } catch (err) {
    console.error(`Error during Redis operations: ${err.message}`);
  } finally {
    // Gracefully close the client
    await client.disconnect();
  }
}

// Execute the main function
main();
