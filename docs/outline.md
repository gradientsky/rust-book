# The Idiomatic Rust Pocket Book — Outline

## Part 1: Why Rust

### Chapter 1: The Rust Philosophy
- 1.1 Zero-cost abstractions: pay only for what you use
- 1.2 Safety without garbage collection
- 1.3 Fearless concurrency
- 1.4 If it compiles, it (usually) works — the compiler as your pair programmer
- 1.5 Rust vs. C/C++, Go, Python, Java — where Rust sits

### Chapter 2: The Toolchain
- 2.1 rustup, rustc, cargo — the holy trinity
- 2.2 Creating, building, running, and testing a project
- 2.3 Crates and crates.io — Rust's package ecosystem
- 2.4 cargo clippy, cargo fmt — linting and formatting
- 2.5 Reading compiler errors (your most important skill)

## Part 2: The Language in a Hurry

### Chapter 3: Types and Variables
- 3.1 Let bindings and immutability by default
- 3.2 Scalar types: integers, floats, bool, char
- 3.3 Compound types: tuples, arrays, slices
- 3.4 Strings: `String` vs `&str` (and why there are two)
- 3.5 Type inference and explicit annotations
- 3.6 Constants and statics

### Chapter 4: Ownership — The Big Idea
- 4.1 What ownership solves (dangling pointers, double frees, data races)
- 4.2 The three rules of ownership
- 4.3 Move semantics: why assignment transfers ownership
- 4.4 Clone vs Copy: explicit vs implicit duplication
- 4.5 References and borrowing: `&T` and `&mut T`
- 4.6 The borrow checker: what it does and how to stop fighting it
- 4.7 Lifetimes in 5 minutes — what `'a` means and when you need it

### Chapter 5: Structs, Enums, and Pattern Matching
- 5.1 Defining structs and impl blocks
- 5.2 Enums: algebraic data types (not just C enums)
- 5.3 `Option<T>` — Rust's null replacement
- 5.4 `Result<T, E>` — errors as values
- 5.5 Pattern matching with `match`, `if let`, `while let`
- 5.6 Destructuring everything

### Chapter 6: Control Flow and Functions
- 6.1 Expressions vs statements (almost everything returns a value)
- 6.2 Functions, closures, and higher-order functions
- 6.3 Iterators: `map`, `filter`, `collect` and the iterator chain
- 6.4 The `?` operator — ergonomic error propagation
- 6.5 Loops: `loop`, `while`, `for`... and `for` is always over an iterator

### Chapter 7: Traits and Generics
- 7.1 Traits: Rust's interfaces (not inheritance)
- 7.2 Implementing traits for your types
- 7.3 Derive macros: getting traits for free (`Debug`, `Clone`, `PartialEq`...)
- 7.4 Generics: writing code that works with many types
- 7.5 Trait bounds: constraining generics
- 7.6 `impl Trait` — the shorthand you'll use everywhere
- 7.7 Trait objects (`dyn Trait`) — when you need dynamic dispatch

## Part 3: Writing Real Code

### Chapter 8: Error Handling Done Right
- 8.1 Panic vs recoverable errors — when to use which
- 8.2 Defining custom error types
- 8.3 The `thiserror` and `anyhow` crates — the community standard
- 8.4 The `?` chain in practice — composing fallible operations

### Chapter 9: Collections and Standard Library Essentials
- 9.1 `Vec<T>`, `HashMap<K,V>`, `HashSet<T>`
- 9.2 Iterating, transforming, collecting
- 9.3 `String` manipulation idioms
- 9.4 File I/O and `std::fs`
- 9.5 Command-line arguments with `std::env`

### Chapter 10: Modules, Crates, and Project Structure
- 10.1 `mod`, `use`, `pub` — visibility and namespacing
- 10.2 File layout conventions (`lib.rs`, `main.rs`, module folders)
- 10.3 Splitting a project into library + binary
- 10.4 Choosing and evaluating third-party crates

### Chapter 11: Testing
- 11.1 `#[test]` and `assert!` — unit tests inline with your code
- 11.2 Integration tests in `tests/`
- 11.3 Doc tests — examples that are also tests
- 11.4 `cargo test` workflows

## Part 4: Thinking in Rust

### Chapter 12: Idiomatic Patterns
- 12.1 Builder pattern — constructing complex objects
- 12.2 Newtype pattern — type safety without overhead
- 12.3 RAII and `Drop` — cleanup that can't be forgotten
- 12.4 State machines with enums
- 12.5 Preferring iteration over indexing
- 12.6 Using `Option` and `Result` combinators instead of unwrap

### Chapter 13: Common Antipatterns to Avoid
- 13.1 Overusing `.clone()` to appease the borrow checker
- 13.2 Reaching for `unwrap()` and `expect()` in library code
- 13.3 Fighting the type system instead of leveraging it
- 13.4 Writing Java/Python/C++ in Rust syntax
- 13.5 Premature `unsafe`

### Chapter 14: Where to Go from Here
- 14.1 Async Rust (tokio, async/await)
- 14.2 Unsafe Rust and FFI
- 14.3 Macros (declarative and procedural)
- 14.4 Concurrency (`Arc`, `Mutex`, channels, Rayon)
- 14.5 The Rust ecosystem: web (Axum), CLI (clap), embedded, Wasm
- 14.6 Recommended reading and community resources
