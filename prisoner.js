let x_ = 0
let y_ = 0

for(let i = 0; i < 10; i++) {
  x = Math.random()
  y = Math.random()

  if(x < 0.5 && y < 0.5) {
    x_ += 1
    y_ += 1
  } else if(x < 0.5 && y > 0.5) {
    x_ += 5
  } else if(x > 0.5 && y < 0.5) {
    y_ += 5
  } else {
    x_ += 3
    y_ += 3
  }
}

console.log(x_, y_)



