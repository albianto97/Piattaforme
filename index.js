const TelegramBot = require('node-telegram-bot-api');
 
// Inseriamo qui il nostro token
const token = '666243794:AAFG3Ww-snpsCBJEZikIOBMLahNYyyOl1ig';
 
// Creiamo il bot
const bot = new TelegramBot(token, {polling: true});
 
// La nostra biografia
const bio = 'Michele Rullo è un ingegnere informatico di Roma, esperto in tecnologie web e mobile.';
 
// La nostra email
const email = 'michele.rullo@hubern.com';
 
// Il progetto a cui stiamo lavorando
const project = 'https://gopaybot.com';
 
// Quando l'utente ci invia il comando /bio, rispondiamo!
// 'msg' è l'oggetto che rappresenta il messaggio inviato dall'utente
bot.onText(/\/bio/, (msg, match) => {
 
  // Su Telegram ogni chat ha un suo numero identificativo. Noi lo utilizziamo
  // per poter rispondere al nostro utente.
  const chatId = msg.chat.id;
 
  // Inviamogli la nostra biografia!
  bot.sendMessage(chatId, bio);
});
 
bot.onText(/\/email/, (msg, match) => {
 
  const chatId = msg.chat.id;
 
  // Inviamogli la nostra email!
  bot.sendMessage(chatId, email);
});
 
bot.onText(/\/project/, (msg, match) => {
 
  const chatId = msg.chat.id;
 
  // Inviamogli il nostro progetto!
  bot.sendMessage(chatId, project);
});
