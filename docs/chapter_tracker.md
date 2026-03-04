# Chapter Tracker

Status legend: **Draft** | **Review** | **Final** | Planned

## Part 1: First Contact

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 1.1 Your First Rust Program | `src/part1/1.1 Your First Rust Program.md` | **Draft** | Philosophy-first intro, install, Cargo, printing/formatting |
| 1.2 The Compiler Is Your Ally | `src/part1/1.2 The Compiler Is Your Ally.md` | **Draft** | Error anatomy (E0382, E0308), warnings, `cargo check`, `cargo clippy`, `cargo fmt`, quality baseline workflow |

## Part 2: Thinking in Values

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 2.1 Variables, Expressions, and Control Flow | `src/part2/2.1 Variables, Expressions, and Control Flow.md` | **Draft** | Immutability, shadowing, scalar types, type inference, constants, expressions, if/loop/while/for, ranges, loop labels, tuples/arrays, if let, let chains (2024) |
| 2.2 Functions and Closures | `src/part2/2.2 Functions and Closures.md` | **Draft** | Functions (params, return, implicit return, early return), expression-oriented bodies, closures (syntax, capture modes, Fn/FnMut/FnOnce traits), higher-order functions, returning closures, function factories |
| 2.3 Ownership | [`src/part2/2.3 Ownership.md`](../src/part2/2.3%20Ownership.md) | **Draft** | Three rules of ownership, stack vs heap, move semantics, Copy types, Clone, Drop/RAII, drop order, early drop, std::mem::drop |
| 2.4 Borrowing and References | [`src/part2/2.4 Borrowing and References.md`](../src/part2/2.4%20Borrowing%20and%20References.md) | **Draft** | Shared refs (`&T`), mutable refs (`&mut T`), many-readers-or-one-writer rule, NLL, borrow checker errors (E0596/E0499/E0502/E0106), slices (`&str`/`&[T]`), dangling references, lifetimes (`'a`), lifetime elision, practical patterns |

## Part 3: Modeling Your Domain

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 3.1 Structs and Methods | [`src/part3/3.1 Structs and Methods.md`](../src/part3/3.1%20Structs%20and%20Methods.md) | **Draft** | Struct definition, field init shorthand, mutation, struct update syntax, tuple structs, unit structs, methods (`&self`/`&mut self`/`self`), associated functions, `new` convention, `#[derive(Debug)]`, `Display` impl, ownership with structs, capstone example |
| 3.2 Enums and Pattern Matching | [`src/part3/3.2 Enums and Pattern Matching.md`](../src/part3/3.2%20Enums%20and%20Pattern%20Matching.md) | **Draft** | ADTs (data-carrying variants, named fields), exhaustive `match` (E0004), match as expression, wildcard `_`, or patterns (`\|`), `if let` / `if let else`, let chains (Rust 2024), destructuring (enums, structs, tuples, nested), match guards, `..` ignore pattern, `Box<Expr>` recursive types, `matches!` macro, capstone Ticket example |
| 3.3 Null, Errors, and the Type System | [`src/part3/3.3 Null, Errors, and the Type System.md`](../src/part3/3.3%20Null,%20Errors,%20and%20the%20Type%20System.md) | **Draft** | `Option<T>` (Some/None, unwrap_or, map, and_then, is_some_and, is_none_or), `Result<T, E>` (Ok/Err, map, map_err, unwrap_or), `?` operator (Result and Option), Option↔Result conversion (ok_or, ok), unwrap/expect guidance, making illegal states unrepresentable (enum vs boolean flags, newtype wrappers, validated construction), capstone Score/grade example |

## Part 4: Abstraction Without Cost

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 4.1 Traits | [`src/part4/4.1 Traits.md`](../src/part4/4.1%20Traits.md) | **Draft** | Trait definition/impl, default methods, `impl Trait` params, derive (`Debug`/`Clone`/`PartialEq`/`Eq`/`Hash`/`Default`/`PartialOrd`/`Ord`/`Copy`), `Display` vs `Debug`, `From`/`Into`, `TryFrom`/`TryInto`, `AsRef`, operator traits (`Add`), orphan rule, capstone temperature conversion example |
| 4.2 Generics | [`src/part4/4.2 Generics.md`](../src/part4/4.2%20Generics.md) | **Draft** | Generic functions/structs/enums, trait bounds (`T: Trait`), `impl Trait` (argument + return position), `where` clauses, associated types vs type params, trait objects (`dyn Trait`), dyn compatibility, monomorphization/zero-cost abstraction, capstone Measurable example |
| 4.3 Iterators and Functional Patterns | [`src/part4/4.3 Iterators and Functional Patterns.md`](../src/part4/4.3%20Iterators%20and%20Functional%20Patterns.md) | **Draft** | Iterator trait (`next`), three iteration modes (iter/iter_mut/into_iter), lazy evaluation, adaptors (map/filter/filter_map/enumerate/zip/take/skip/flatten/flat_map/chain/inspect), consumers (collect/fold/sum/product/count/any/all/find/position/min/max), collecting into Vec/String/HashMap/HashSet/Result, ranges as iterators, `repeat_n`/`once`/`from_fn`/`successors`, implementing Iterator for custom types, IntoIterator, `is_sorted_by_key` (1.82), capstone GradeBook example |

## Part 5: Building Real Things

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 5.1 Error Handling in Practice | [`src/part5/5.1 Error Handling in Practice.md`](../src/part5/5.1%20Error%20Handling%20in%20Practice.md) | **Draft** | `Error` trait (Debug+Display, `source()`), error chains, thiserror 2.x (`#[error]`/`#[from]`/`#[source]`/`#[error(transparent)]`), anyhow 1.x (`Result`, `Context`/`with_context`, `bail!`/`ensure!`/`anyhow!`), `?` and `From::from()` composition, library vs application error strategy, unwrap spectrum, capstone Inventory example |
| 5.2 Collections, Strings, and Smart Pointers | [`src/part5/5.2 Collections, Strings, and Smart Pointers.md`](../src/part5/5.2%20Collections,%20Strings,%20and%20Smart%20Pointers.md) | **Draft** | Vec (creation/access/modify/slices/iteration), HashMap (creation/get/entry API), HashSet (membership/set ops), String vs &str (ownership/conversion/UTF-8), Box (recursive types/trait objects), Rc (shared ownership/refcount), Arc (thread-safe shared ownership), capstone Library/Document tag system |
| 5.3 Modules and Project Structure | — | Planned | mod/use/pub, Cargo.toml, workspaces |
| 5.4 Testing as a First-Class Citizen | — | Planned | Unit/integration/doc tests, cargo test |

## Part 6: Fearless Systems Programming

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 6.1 Concurrency Without Data Races | — | Planned | Threads, Send/Sync, Arc/Mutex, channels, async taste |

## Part 7: Idiomatic Rust

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 7.1 Patterns the Pros Use | — | Planned | Builder, newtype, type-state, combinators |
| 7.2 What Not to Do | — | Planned | Anti-patterns, common mistakes |
| 7.3 Where to Go from Here | — | Planned | Async, unsafe, macros, ecosystem, resources |
