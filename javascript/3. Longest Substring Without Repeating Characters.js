// find longest subsing
let testsing1 = "abcabcbb";
let testsing2 = "bbbbb";
let testsing3 = "pwwkew";
let testsing4 = "dvdf";

function counter(s) {
    arr = [];
    let maxnumb = 0;
    for (i in s) {
        if (arr.includes(s[i])) {
            maxnumb = (arr.length > maxnumb) ? arr.length : maxnumb;
            arr = arr.slice(arr.indexOf(s[i])+1, arr.length);
        };
        arr.push(s[i]);
    }
    maxnumb = (arr.length > maxnumb) ? arr.length : maxnumb;
    return maxnumb;
}

console.log(counter(testsing1));
console.log(counter(testsing2));
console.log(counter(testsing3));
console.log(counter(testsing4));
