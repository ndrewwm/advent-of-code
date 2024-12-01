const { default: fs } = await import("node:fs");

// Cleanup
let data = fs.readFileSync("../data/day1.txt", "utf-8");
let rows = data.split("\n").map((row) => row.split(" "));
let day1 = {
  left: rows.map((row) => Number(row.at(0))).sort(),
  right: rows.map((row) => Number(row.at(-1))).sort(),
};

// Part 1
let out = [];
for (let i = 0; i < rows.length; i++) {
  out.push({
    l: day1.left.at(i),
    r: day1.right.at(i),
    d: day1.left.at(i) - day1.right.at(i),
  });
}

let total = 0;
for (item of out) {
  total += Math.abs(item.d);
}
console.log(total); // 3569916 correct

// Part 2
let total2 = 0;
for (let entry of out) {
  let count = 0;
  day1.right.map((right) => {
    count += entry.l === right ? 1 : 0;
  });
  total2 += entry.l * count;
}
console.log(total2); // 26407426 correct
