import fs from "node:fs";

const data = fs.readFileSync("../data/day-1.txt", "utf-8");

// PART 1

function solve_part1(txt) {
    const out = txt.replace(/[a-z]/g, "")
        .split("\n")
        .map((str) => str[0] + str[str.length - 1])
        .map(Number)
        .reduce((total, amount) => total + amount);

    return out;
}

console.log(solve_part1(data));

// PART 2


function solve_part2(txt) {
    let out = txt.replaceAll(/twone/g, "2")
        .replaceAll(/threeight/g, "3")
        .replaceAll(/fiveight/g, "5")
        .replaceAll(/sevenine/g, "7")
        .replaceAll(/eightwo/g, "8")
        .replaceAll(/eighthree/g, "8")
        .replaceAll(/nineight/g, "9");
        
    let digits = [
        ["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"],
        ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"],
    ];

    for (const [digit, num] of digits) {
        out = out.replaceAll(digit, num);
    }

    return solve_part1(out);
}

console.log(solve_part2(data));
// 54305 is wrong
