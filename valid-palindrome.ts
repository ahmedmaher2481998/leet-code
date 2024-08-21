function isPalindrome(s: string) {
  const res = s.replace(/[^a-zA-Z0-9]/gi, "").toLowerCase();
  return res === res.split("").reverse().join("");
}

console.log(
  "first test is true: ",
  isPalindrome("A man, a plan, a canal: Panama")
);
const s2 = "race a car";
console.log("second test is false: ", isPalindrome(s2));
const s3 = " ";
console.log("first test is true: ", isPalindrome(s3));
