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
| 2.4 Borrowing and References | — | Planned | References, borrow checker, lifetimes intro |

## Part 3: Modeling Your Domain

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 3.1 Structs and Methods | — | Planned | Structs, impl blocks, derive Debug, Display |
| 3.2 Enums and Pattern Matching | — | Planned | ADTs, match, if let, let chains (2024), destructuring |
| 3.3 Null, Errors, and the Type System | — | Planned | Option, Result, `?` operator, making illegal states unrepresentable |

## Part 4: Abstraction Without Cost

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 4.1 Traits | — | Planned | Trait definition/impl, derive, std conversion traits |
| 4.2 Generics | — | Planned | Generics, trait bounds, impl Trait, dyn Trait |
| 4.3 Iterators and Functional Patterns | — | Planned | Iterator adaptors, lazy evaluation, collect |

## Part 5: Building Real Things

| Chapter | File | Status | Notes |
|---------|------|--------|-------|
| 5.1 Error Handling in Practice | — | Planned | Custom errors, thiserror, anyhow |
| 5.2 Collections, Strings, and Smart Pointers | — | Planned | Vec, HashMap, String/&str, Box/Rc/Arc |
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
