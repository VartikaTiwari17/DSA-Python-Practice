var minOperations = function(s) {
const n = s.length;
const sorted = s.split('').sort().join('');


if (s === sorted) return 0;

if (n === 2) return -1;

const minChar = sorted[0];
const maxChar = sorted[n - 1];

if (s[0] === minChar || s[n - 1] === maxChar) {
    return 1;
}

if (s[0] === maxChar && s[n - 1] === minChar) {
    let minCount = 0;
    let maxCount = 0;

    for (const ch of s) {
        if (ch === minChar) minCount++;
        if (ch === maxChar) maxCount++;
    }

    if (minCount === 1 && maxCount === 1) {
        return 3;
    }

    return 2;
}

return 2;


};
