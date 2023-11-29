// function name(params) {
//     if(true){
//         let x="Hello world";
//         console.log(x);
//     }
// }
// console.log(name());

// let---> chabgeable
// const---> Unchangeable

const test="World";
const name= `Hello ${test}`;
console.log(name);

const num=[1,2,3,4,5,15];
const newArray=["Rahim", "Salam", ...num];
console.log(newArray);

// its showing in the console---> ['Rahim', 'Salam', 1, 2, 3, 4, 5, 15]

console.log(Math.max(...num));

// Regular function

function test2(params) {
    return "Hi, I am normal fumction";
    
}
const result=test2();
console.log(result);


// Arrow Function

const test3=()=>"Hi, I am single line Arrow function";
console.log(test3());

const test4 = () => {
    console.log("Hey, I am multi line Arrow function");
    return "Yes boss";
};
console.log(test4());