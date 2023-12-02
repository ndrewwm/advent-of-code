import fs from "node:fs";

const data = fs.readFileSync("../data/day-2.txt", "utf-8");

const N_RED = 12;
const N_GREEN = 13;
const N_BLUE = 14;

function clean_data(puzzle) {
    puzzle = puzzle.replace(/Game (.*): /g, "")
        .split("\n")
        .map((game) => {
            const sets = game.split("; ")
                .map((set) => set.split(", "))
                .map((set) => {
                    let values = {};
                    for (const item of set) {
                        const [n, color] = item.split(" ");
                        values[color] = Number(n);
                    }
                    return values;
                });
            return sets;
        });

    return puzzle;
}

function solve_part1(games) {
    const impossible = games.map((game) => {
        const r = game.map((item) => item.red);
        const g = game.map((item) => item.green);
        const b = game.map((item) => item.blue);

        let out = r.some((x) => x > N_RED);
        out = out || g.some((x) => x > N_GREEN);
        out = out || b.some((x) => x > N_BLUE);

        return out;
    });

    var out = [];
    for (let i = 0; i < 100; i++) {
        if (impossible[i]) out.push(i + 1);
    }

    return out.reduce((total, item) => total + item);
}

// 2207: incorrect
// 2255: incorrect
console.log(solve_part1(clean_data(data)));