import { createClient } from 'redis';

const subscriber = createClient({
  url: 'redis://127.0.0.1:6379',
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

subscriber.connect().then(() => {
  subscriber.subscribe('ALXchannel', (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe('ALXchannel').then(() => subscriber.quit());
    }
  });
});
