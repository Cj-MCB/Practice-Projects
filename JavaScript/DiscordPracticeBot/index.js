require('dotenv').config(); //Initialize dotenv
const Discord = require('discord.js'); //Import Discord.js

const client = new Discord.Client({intents: [Discord.GatewayIntentBits.Guilds, Discord.GatewayIntentBits.GuildMessages]}); // Creates new Discord Client

client.on('ready', () => {
    console.log(`Bot logged in as ${client.user.tag}.`)
});

console.log(process.env.CLIENT_TOKEN)
client.login(process.env.CLIENT_TOKEN); // Logs bot in with token