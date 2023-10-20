
# Table of Contents
1. [Rust Notes](#rust-notes)
2. [This Cache-Sim](#this-cache-sim)



## Rust Notes
* statically typed language: must know the type of variable at compile time

  eg.  ```rust let guess: u32 = "42".parse().expect("Not a number!");```

* data types:

   - int (default i32)
 
   ![image](https://github.com/Elle-Wen/cache-sim/assets/70612012/dacb599c-05db-422c-97c2-5c28e0edcc13)

  - float: f32, f64

  - bool

  - char: use single quotes

  - tuple: group different types of values; fix length

  eg.

  ```
  let tup: (i32, f64, u8) = (500, 6.4, 1); //declare
  let (x, y, z) = tup;//pattern matching, destruting
  let five_hundred = x.0;//access
  ```

  - array: group same types of values; fix length

  eg. ```let a: [i32; 5] = [1, 2, 3, 4, 5];```

* function:
  ```
  fn exampe(param_1:type_1, param_2,type_2) -> return_type{
  }
  ```
  - expression (has a returned value, no ;) vs. statements (just action, no result, has ;)

* control flow

  - expression, not statement
    ```let number = if condition { 5 } else { 6 };```

  - loop can return value
    ```
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };
    ```
  - loop label start with '
* ownership
  - all heap data must be owned by 1 variable 
  - ```let a = Box::new(things)//put things into heap, a is a pointer，has ownership```
  - When a is bound to ```Box::new([0; 1_000_000])```, we say that a owns the box. The       statement ```let b = a``` moves ownership of the box from a to b
  - If a variable owns a box, when Rust deallocates the variable's frame, then Rust   deallocates the box's heap memory
  - variables can't be used after being moved (i.e has transfered ownership to other variables)
  - ```variable.clone(origianl)//deep copy, creates a copy of the things in the heap```
  - ```&variable``` for non-owning pointers； used with *variable
  - data should not be aliased and mutated 
  - default variable: Read and Own; let mut variable: ROW
  - slices: can point to part of the things in heap
    ```
    let s = String::from("hello world")
    let hello: &str = &s[0..5];
    ```
* struct
  - struct update syntax
     ```
     fn main() {
      // --snip--
      let user2 = User {
          email: String::from("another@example.com"),
          ..user1
         }
      };
    ```
  - method
    ```
    struct Rectangle {
    width: u32,
    height: u32,
    }
    impl Rectangle {
        fn area(&self) -> u32 {
            self.width * self.height
        }
    }
* package and crate menagement
  - crate root file: src/main.rs; lib root file: src/lib.rs
  - :: path identifiers 
  
## This Cache-Sim
* main.rs
  
  - run with ```cargo run atf_file(no extention) prefix_length Optional_flags```

  - always output to "stack-distances.csv" file that has header: Name, Trace length, Unique items (prefix length),Unique strides (prefix length),Prefix,Item entropy,Stride entropy,Item conditional entropy,Stride conditional entropy,Exponential function entropy,Linear Function entropy,Infinities,Stack distances
  - Flag L: write one line to "linear-function-data.csv" file that has header: Name,Trace length,Continuations of 1, Continuations of 2,...
  - Flag H: output "atf_file-histograms.csv" file under histograms/frequency-histograms that has the format: ![image](https://github.com/Elle-Wen/cache-sim/assets/70612012/1c7e109d-a6c7-40fe-a77d-5a4d7d63ca1c)
  - Flag S: print stack distance out in "stack-distances.csv" file, if absent, print 0
  - Flag P: paging model true
  - Flag C: continuation true
* histogram_maker.py
  - run with ```python3 ./src/histogram_maker.py [T/H/L(data style)] [filename(extention)] [plot style for H/L] [name of plot]```
  - T style: stack distance vs. frequency
  - H style: entropy vs. frequency (NOT WORKING)
  - L style: streak size vs frequency (NOT WORKING) 

  
