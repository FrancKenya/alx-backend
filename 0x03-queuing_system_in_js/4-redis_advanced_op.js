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

const setHash = () => {
  client.hset('ALX', 'Portland', 50, redis.print);
  client.hset('ALX', 'Seattle', 80, redis.print);
  client.hset('ALX', 'New York', 20, redis.print);
  client.hset('ALX', 'Bogota', 20, redis.print);
  client.hset('ALX', 'Cali', 40, redis.print);
  client.hset('ALX', 'Paris', 2, redis.print);
};

const displayHash = () => {
  client.hgetall('ALX', (err, res) => {
    if (err) {
      console.error(`Error: ${err.message}`);
      return;
    }
    console.log(res);
  });
};

setHash();
displayHash();
