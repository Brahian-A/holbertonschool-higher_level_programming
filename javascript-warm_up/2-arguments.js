#!/usr/bin/node

const args = process.argv.slice(2); // nos saltamos los dos primeros porque el primero tiene la ruta para ejercutar node y el segundo tiene la ruta al archivo js

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
