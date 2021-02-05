const Discord = require('discord.js');
const client = new Discord.Client();
let fs = require('fs');
let request = require('request');

const app = require('express')();
const {PythonShell} = require('python-shell');


function run_file(){
    PythonShell.run('predict_image.py', null, function (err, results) {
    });
}


function download(url){
    request.get(url)
        .on('error', console.error)
        .pipe(fs.createWriteStream('num.png'));
}

function finish(msg){
    const txt = fs.readFileSync('./res.txt','utf8');
    msg.channel.send('Predicted number as ' + txt);
}



client.once('ready', ()=>{
    console.log("keith is online");

});


client.on('message', msg => {
    
	if (msg.content=== 'test') {
		msg.channel.send(':eyes:');
	}
    if(msg.attachments.first()){//checks if an attachment is sent
        msg.channel.send('downloading content');
        download(msg.attachments.first().url);
        run_file()
        
    }
    if (msg.content=== 'predict') {
        setTimeout(() => {  console.log("Loaded"); }, 2000);
		finish(msg);
	}
    

});








client.login('ODA2OTkxNjcxNTgwODE5NDY2.YBxfjw.ZWcrZ4eWUBtfFK5aRAYC_NCOMeQ');