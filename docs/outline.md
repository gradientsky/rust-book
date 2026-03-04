# The Idiomatic Rust Pocket Book

> The most condensed path from zero to idiomatic, production-grade Rust 2024.

## Guiding Principles

- **Philosophy first.** Every chapter opens with _why_ before _what_ or _how_.
  The reader should understand the design intent behind Rust's choices before
  learning the syntax that expresses them.
- **Gradual without overload.** Each chapter introduces exactly one major idea
  and the minimum supporting concepts needed to use it. No forward references
  to unexplained features. No "we'll cover this later" — if it appears, it's
  explained enough to use _now_.
- **Beginner-friendly, production-grade.** The code a reader writes on page 10
  should be the _same_ code they'd write in a production codebase. No training
  wheels to unlearn later. Rust 2024 edition idioms from day one.
- **Show, then name.** Introduce the behavior first with a concrete example,
  then give it its technical name. Not the other way around.
- **Rust 2024 throughout.** All code targets `edition = "2024"` (Rust 1.85+).
  Where the 2024 edition changes behavior — `let` chains, stricter `unsafe`
  scoping, revised temporary lifetimes — this book teaches the 2024 way as the
  _only_ way. No "in previous editions" digressions.

---

## Part 1: First Contact

### Your First Rust Program

Why Rust exists — the gap it fills between safe-but-slow and fast-but-dangerous.
Install the toolchain with rustup. Create a project with **`cargo new`** and
`edition = "2024"` in _Cargo.toml_ — what an edition is and why it matters (one
paragraph, not a history lesson). Run hello world. Anatomy of a Rust program:
`fn main`, `println!`, semicolons. Printing and formatting: `println!` with `{}`
placeholders, `{:?}` for debug output. The reader walks away with a working
environment and the confidence that they can build and run code.

### The Compiler Is Your Ally

Rust's most unusual trait: the compiler catches bugs _before_ your code runs.
Read a compiler error, understand what it's telling you, and fix it. Introduce
`cargo check` as the fastest feedback loop. Show the difference between Rust
errors and the errors readers are used to from other languages — Rust's are
specific, actionable, and trustworthy. Introduce `cargo clippy` and `cargo fmt`
as the quality baseline every Rust project uses from day one.

---

## Part 2: Thinking in Values

### Variables, Expressions, and Control Flow

Everything is immutable by default, and that's a feature, not a limitation.
`let` bindings, `mut`, shadowing. Scalar types (integers, floats, `bool`,
`char`) and type inference — Rust figures out the types so you usually don't
have to write them. Constants and statics.

Then the key insight that separates Rust from C-family languages: _almost
everything is an expression that returns a value_. `if` returns a value. Blocks
return their last expression. Even `match` is an expression. Demonstrate with
`let status = if condition { "ok" } else { "fail" };` — no ternary operator
needed because `if` already is one.

Control flow: `if`/`else`, `loop`, `while`, `for`. Every `for` loop iterates
over an iterator — there is no C-style `for(i=0; i<n; i++)`. Ranges as the
idiomatic way to loop over numbers. `let` chains in `if` and `while` conditions
for combining boolean tests with pattern matching (Rust 2024).

### Functions and Closures

Functions as the primary unit of code organization. Parameters, return types,
and the implicit return of the last expression (no `return` keyword needed in
most cases). Closures: anonymous functions that capture their environment. The
three capture modes and why they matter — but let the compiler figure it out
for now. Higher-order functions: passing functions and closures as arguments.

### Ownership

The single most important idea in Rust. Start with the problem: what goes wrong
without it — dangling pointers, double frees, use-after-free, data races. Then
the solution: every value has exactly one owner, and when the owner goes out of
scope, the value is cleaned up automatically and deterministically.

Build the mental model: stack vs heap. Why integers live on the stack and strings
live on the heap. Why this distinction matters for performance and for
understanding when data moves vs copies.

Move semantics: why `let b = a` transfers ownership of heap data instead of
copying it. `Copy` types: small, stack-only values that are duplicated
implicitly. `Clone`: explicit, potentially expensive duplication when you
actually need a copy.

`Drop` and deterministic destruction: when a value's owner goes out of scope,
Rust runs its destructor automatically. No garbage collector, no finalizer
uncertainty. This is RAII — resource acquisition is initialization — and it
applies to files, network connections, locks, and every other resource.

### Borrowing and References

You can look at a value without taking ownership of it. Shared references
(`&T`) and exclusive references (`&mut T`). The rule: many readers _or_ one
writer, never both at the same time. Show how this single rule prevents data
races at compile time — no runtime cost.

The borrow checker: what it checks, how to read its errors, and how to work
_with_ it instead of fighting it. Common patterns that satisfy the borrow
checker. When the compiler says no, it's usually pointing you toward a better
design.

Lifetimes: what `'a` means, why it exists, and that the compiler infers
lifetimes for you in the vast majority of cases. The reader should understand
the _concept_ without memorizing lifetime elision rules.

---

## Part 3: Modeling Your Domain

### Structs and Methods

Group related data into a struct. Attach behavior with `impl` blocks. The
difference between methods (`&self`, `&mut self`, `self`) and associated
functions (no `self`). How Rust replaces constructors: the `new` convention, and
why there's no special constructor syntax. Printing your types: `#[derive(Debug)]`
to get `{:?}` formatting, and implementing `Display` when you want user-facing
output with `{}`.

### Enums and Pattern Matching

Enums that carry data — algebraic data types. Why this is fundamentally
different from enums in C or Java: each variant can hold different data. `match`
as exhaustive pattern matching — the compiler guarantees you handle every case.
`if let` for when you only care about one variant. `let` chains for combining
multiple patterns with boolean conditions (Rust 2024). Destructuring in all its
forms: structs, tuples, nested enums.

### Null, Errors, and the Type System

The philosophy: _if a function can fail, its signature must say so_. Two
examples that changed everything:

`Option<T>` replaces null — a value is either `Some(T)` or `None`, and you
must handle both cases. `Result<T, E>` replaces exceptions — an operation either
succeeds with `Ok(T)` or fails with `Err(E)`, and the compiler forces you to
deal with the error. The `?` operator for ergonomic error propagation: try the
operation, return early on error, or unwrap the success value — all in one
character.

Then the deeper principle: _making illegal states unrepresentable_. Use the type
system so that invalid states simply cannot compile. An enum with three variants
replaces a boolean flag and a nullable field. A newtype wrapper prevents mixing
up user IDs and order IDs. The compiler becomes a proof assistant for your domain
logic.

---

## Part 4: Abstraction Without Cost

### Traits

The philosophy: shared behavior without inheritance hierarchies. Define a trait,
implement it for your types. Why traits are more flexible than interfaces in Java
or protocols in Swift — any type can implement any trait, even types you didn't
write.

Derive macros: getting `Debug`, `Clone`, `PartialEq`, `Hash` for free with a
single annotation. The standard formatting traits: `Debug` for developers
(`{:?}`), `Display` for users (`{}`), and how to implement both.

Standard conversion traits: `From` and `Into` for type conversions that cannot
fail. `TryFrom` and `TryInto` when conversion might fail. `AsRef` and `AsMut`
for cheap reference-to-reference conversions. These traits are the glue that
makes Rust APIs feel ergonomic — understand them and every library becomes more
natural to use.

### Generics

Write code once, use it with many types — with no runtime cost. How generics and
trait bounds work together: `fn process<T: Display>(item: T)`. `impl Trait` as
the shorthand you will use everywhere: in argument position and in return
position.

Trait objects (`dyn Trait`) and when you need dynamic dispatch — rare, but
important when you do. Zero-cost abstraction: generics compile to the same
machine code you would write by hand for each concrete type.

### Iterators and Functional Patterns

The iterator pattern: `map`, `filter`, `fold`, `collect`, and chaining. Why
Rust iterators are both more ergonomic _and_ faster than manual indexed loops —
the compiler optimizes iterator chains into the same tight loops you would write
in C. Lazy evaluation: nothing happens until you consume the iterator.

Collecting into different types. `enumerate`, `zip`, `take`, `skip`, `flatten`.
The `Iterator` trait and why implementing it unlocks the entire ecosystem of
adaptors for your custom types.

---

## Part 5: Building Real Things

### Error Handling in Practice

Building on the `Result` and `?` foundation from Part 3. Defining custom error
types with enums. The ecosystem standard: thiserror for library crates (derive
macro for error types), anyhow for application crates (when you just need the
error message, not the type). Composing fallible operations with `?` chains.
When to use `unwrap` (tests and prototyping) vs `expect` (with a message
explaining the invariant) vs proper error handling.

### Collections, Strings, and Smart Pointers

`Vec<T>`, `HashMap<K, V>`, `HashSet<T>` — the workhorses. Iterating,
transforming, and collecting. Slices (`&[T]`) as the universal view into
contiguous data.

`String` vs `&str` revisited in depth: owned vs borrowed, heap-allocated vs
a view into existing data. Why Rust has two string types and when to use each.
Common string manipulation idioms.

Smart pointers: `Box<T>` for heap allocation and recursive types. `Rc<T>` for
shared ownership within a single thread. `Arc<T>` for shared ownership across
threads. When you need each one, and why the default should be regular ownership
and borrowing — reach for smart pointers only when the simpler model doesn't fit.

### Modules and Project Structure

Organizing code as projects grow: `mod`, `use`, `pub` — visibility and
namespacing. File layout conventions in Rust 2024 (`lib.rs`, `main.rs`,
module folders). Splitting a project into a library and a binary crate.
Workspaces for multi-crate projects.

_Cargo.toml_ in depth: `edition = "2024"`, dependency declarations,
`[features]`, the Rust 2024 resolver (v3) and what it does. Choosing and
evaluating third-party crates: docs.rs, lib.rs, download counts, maintenance
signals.

### Testing as a First-Class Citizen

Rust builds testing into the language and toolchain, not bolted on as an
afterthought. Unit tests inline with your code (`#[test]`, `assert!`,
`assert_eq!`). Integration tests in the _tests/_ directory. Doc tests: code
examples in documentation comments that are compiled and run as tests — keeping
examples honest forever.

`cargo test` workflows: running specific tests, filtering, showing output,
ignoring slow tests. Testing error cases with `#[should_panic]` and returning
`Result` from tests.

---

## Part 6: Fearless Systems Programming

### Concurrency Without Data Races

The philosophy: concurrency should be _safe by default_. Rust's ownership and
borrowing rules — the same ones you've already learned — prevent data races at
compile time. No runtime overhead, no locks you forgot to acquire.

Threads with `std::thread::spawn`. The `Send` and `Sync` traits: the compiler
checks at compile time whether a type is safe to send across threads or share
between them. You don't implement these traits manually — the compiler derives
them automatically from a type's fields.

Shared state: `Arc<T>` for shared ownership across threads, `Mutex<T>` for
interior mutability. Message passing with channels (`std::sync::mpsc`). When to
use shared state vs message passing.

A taste of async: `async`/`await` syntax, what a future is, why you need a
runtime (tokio). Async closures (Rust 2024). Enough to understand async code
when you encounter it, with pointers to go deeper.

---

## Part 7: Idiomatic Rust

### Patterns the Pros Use

Builder pattern for constructing complex objects. Newtype pattern for type
safety at zero cost. Type-state pattern: using the type system to enforce valid
state transitions at compile time. Preferring iterators over indexing. Using
`Option` and `Result` combinators (`map`, `and_then`, `unwrap_or_else`) instead
of `match` on every call. Extension traits for adding methods to types you
don't own.

### What Not to Do

Cloning everything to make the borrow checker happy — what to do instead.
Reaching for `unwrap()` in library code. Fighting the type system instead of
leveraging it. Writing Java/Python/C++ translated literally into Rust syntax:
overusing `dyn Trait`, deep inheritance-like hierarchies, getter/setter
boilerplate. Reaching for `unsafe` before exhausting safe alternatives.

### Where to Go from Here

Async Rust in depth: tokio, the async ecosystem, structured concurrency.
Unsafe Rust: what it unlocks, why it exists, how to use it responsibly. The
Rust 2024 safety improvements: `unsafe_op_in_unsafe_fn`, `unsafe extern`
blocks, the end of `static mut` references. Declarative and procedural macros.
The Rust ecosystem: web servers (Axum, Actix), CLI tools (clap), serialization
(serde), embedded, WebAssembly. Recommended reading and community resources.
