#!/usr/bin/node

const argumentCounter = process.argv.length;

if (argumentCounter === 2)
{
    console.log('No argument');
}
else if (argumentCounter === 3)
{
    console.log('Argument found');
}
else 
{
    console.log('Arguments found');
}