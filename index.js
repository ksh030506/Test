const Pythonshell = require("python-shell");
const fs = require("fs");

// nodejs에서 이미지파일 받기
var data = fs.readFileSync("image/image.png");

pyshell = new Pythonshell.PythonShell("./cyclegan.py");

//json으로 묶어준다.
dat = {
  binary: data
};

//json으로 submit
dat_json = JSON.stringify(dat);
console.log(typeof(dat_json));
pyshell.send(dat_json, { mode: "json" });

//python에서 가공후
//string 형태의 json으로 반환.
pyshell.on("message", results => {
  //다시 json으로 변환후 획득
 var imgdata = JSON.parse(results).img;
 console.log(imgdata);
  
//imgdata는 이진정보를 리스트로 담고 있기 때문에
// Buffer 타입으로 변환시켜준다.
imbuffer = new Buffer.from(imgdata);

const upload = './upload/';

// local write
// 이미지를 로컬에 저장하여 확인해본다.
fs.writeFileSync(upload + "temp.jpeg", imbuffer);
console.log("complete");
});

//error 처리
pyshell.end(err => {
  if (err) {
    console.log(err);
  }
});