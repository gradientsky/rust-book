# References

Resources used to build book materials, organized by topic.

---

## Rust 2024 Edition

- [Announcing Rust 1.85.0 and Rust 2024 | Rust Blog](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/)
- [Rust 2024 - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/index.html)
- [let chains in if and while - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/let-chains.html)
- [Cargo: Rust-version aware resolver - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/cargo-resolver.html)
- [Rustfmt: Formatting fixes - The Rust Edition Guide](https://doc.rust-lang.org/stable/edition-guide/rust-2024/rustfmt-formatting-fixes.html)
- [Tail expression temporary scope - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/temporary-tail-expr-scope.html)

## Installation and Tooling

- [Install Rust - Rust Programming Language](https://rust-lang.org/tools/install/)
- [Installation - The Rust Programming Language](https://doc.rust-lang.org/book/ch01-01-installation.html)
- [cargo-new(1) - The Cargo Book](https://doc.rust-lang.org/cargo/commands/cargo-new.html)
- [First Steps with Cargo - The Cargo Book](https://doc.rust-lang.org/cargo/getting-started/first-steps.html)
- [Hello, Cargo! - The Rust Programming Language](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html)
- [The Manifest Format - The Cargo Book](https://doc.rust-lang.org/cargo/reference/manifest.html)

## Rust Release History

- [Announcing Rust 1.93.1](https://blog.rust-lang.org/2026/02/12/Rust-1.93.1/)
- [Rust 1.94.0 Release Notes](https://github.com/rust-lang/rust/issues/151650)
- [The Rust Release Announcements](https://blog.rust-lang.org/releases/)

## Printing and Formatting

- [std::fmt module - Rust std docs](https://doc.rust-lang.org/std/fmt/index.html)
- [format! macro - Rust std docs](https://doc.rust-lang.org/std/macro.format.html)
- [Formatting syntax - The Rust Reference](https://doc.rust-lang.org/std/fmt/index.html#syntax)

## Compiler Errors and Diagnostics

- [E0382 Error Code Reference](https://doc.rust-lang.org/error_codes/E0382.html)
- [E0308 Error Code Reference](https://doc.rust-lang.org/error_codes/E0308.html)
- [Comparing Compiler Errors Across Languages - Amazing CTO](https://www.amazingcto.com/developer-productivity-compiler-errors/)
- [The Most Common Rust Compiler Errors - JetBrains RustRover Blog](https://blog.jetbrains.com/rust/2023/12/14/the-most-common-rust-compiler-errors-as-encountered-in-rustrover-part-1/)

## Clippy and Formatting

- [Clippy Usage - Official Docs](https://doc.rust-lang.org/clippy/usage.html)
- [Clippy Lints Reference](https://rust-lang.github.io/rust-clippy/master/index.html)
- [rustup Profiles - Default Components](https://rust-lang.github.io/rustup/concepts/profiles.html)
- [Rustfmt: Style Edition - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/rustfmt-style-edition.html)
- [cargo check - The Cargo Book](https://doc.rust-lang.org/cargo/commands/cargo-check.html)

## Constants and Statics

- [const keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.const.html)
- [static keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.static.html)
- [RFC 0246: const vs static](https://rust-lang.github.io/rfcs/0246-const-vs-static.html)
- [Disallow references to static mut - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/static-mut-references.html)
- [LazyLock in std::sync - Rust std docs](https://doc.rust-lang.org/std/sync/struct.LazyLock.html)
- [AtomicU32 in std::sync::atomic - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU32.html)
- [Ordering in std::sync::atomic - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html)

## Integer Overflow

- [RFC 0560 - Integer Overflow](https://rust-lang.github.io/rfcs/0560-integer-overflow.html)
- [Data Types: Integer Overflow - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-02-data-types.html#integer-overflow)

## Integer Methods

- [u32::is_multiple_of - Rust Standard Library](https://doc.rust-lang.org/std/primitive.u32.html#method.is_multiple_of) — stabilized Rust 1.87.0
- [Tracking Issue #128101 - unsigned_is_multiple_of](https://github.com/rust-lang/rust/issues/128101)
- [u32::midpoint - Rust Standard Library](https://doc.rust-lang.org/std/primitive.u32.html#method.midpoint) — stabilized Rust 1.85.0 (unsigned), Rust 1.87.0 (signed)
- [Tracking Issue #110840 - num_midpoint](https://github.com/rust-lang/rust/issues/110840)
- [Announcing Rust 1.85.0 (unsigned/float midpoint)](https://blog.rust-lang.org/2025/02/20/Rust-1.85.0/)
- [Announcing Rust 1.87.0 (signed midpoint)](https://blog.rust-lang.org/2025/05/15/Rust-1.87.0/)
- [i32::checked_add - Rust std docs](https://doc.rust-lang.org/std/primitive.i32.html#method.checked_add)
- [i32::saturating_add - Rust std docs](https://doc.rust-lang.org/std/primitive.i32.html#method.saturating_add)
- [i32::wrapping_add - Rust std docs](https://doc.rust-lang.org/std/primitive.i32.html#method.wrapping_add)
- [i32::strict_add - Rust std docs](https://doc.rust-lang.org/std/primitive.i32.html#method.strict_add)
- [Stabilize strict_overflow_ops (PR #144682)](https://github.com/rust-lang/rust/pull/144682)
- [Announcing Rust 1.91.0 (strict_overflow_ops) - Rust Blog](https://releases.rs/docs/1.91.0/)
- [Cargo Profiles: overflow-checks - The Cargo Book](https://doc.rust-lang.org/cargo/reference/profiles.html)
- [u8::cast_signed - Rust Standard Library](https://doc.rust-lang.org/std/primitive.u8.html#method.cast_signed) — stabilized Rust 1.87.0
- [i32::cast_unsigned - Rust Standard Library](https://doc.rust-lang.org/std/primitive.i32.html#method.cast_unsigned) — stabilized Rust 1.87.0
- [Tracking Issue #125882 - integer_sign_cast](https://github.com/rust-lang/rust/issues/125882)
- [Announcing Rust 1.87.0 (cast_signed/cast_unsigned)](https://blog.rust-lang.org/2025/05/15/Rust-1.87.0/)

## Variables, Types, and Expressions

- [Variables and Mutability - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [Data Types - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [Expressions - Rust By Example](https://doc.rust-lang.org/rust-by-example/expression.html)
- [Block expressions - The Rust Reference](https://doc.rust-lang.org/reference/expressions/block-expr.html)
- [Scope and Shadowing - Rust By Example](https://doc.rust-lang.org/rust-by-example/variable_bindings/scope.html)
- [const keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.const.html)
- [static keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.static.html)

## Control Flow and Loops

- [for and range - Rust By Example](https://doc.rust-lang.org/rust-by-example/flow_control/for.html)
- [Returning from loops - Rust By Example](https://doc.rust-lang.org/rust-by-example/flow_control/loop/return.html)
- [Loop expressions - The Rust Reference](https://doc.rust-lang.org/reference/expressions/loop-expr.html)

## Let Chains (Rust 2024)

- [let chains in if and while - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/let-chains.html)
- [Announcing Rust 1.88.0 | Rust Blog](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
- [RFC 2497: if- and while-let-chains](https://rust-lang.github.io/rfcs/2497-if-let-chains.html)

## Functions and Closures

- [Functions - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Constant evaluation - The Rust Reference](https://doc.rust-lang.org/reference/const_eval.html)
- [const keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.const.html)
- [Closures - The Rust Programming Language](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Advanced Functions and Closures - The Rust Programming Language](https://doc.rust-lang.org/book/ch20-04-advanced-functions-and-closures.html)
- [Closure types - The Rust Reference](https://doc.rust-lang.org/reference/types/closure.html)
- [Closures - Rust By Example](https://doc.rust-lang.org/rust-by-example/fn/closures.html)
- [Changes to impl Trait in Rust 2024 - Rust Blog](https://blog.rust-lang.org/2024/09/05/impl-trait-capture-rules/)
- [RPIT Lifetime Capture Rules - The Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/rpit-lifetime-capture.html)
- [RFC 3668: Async Closures - The Rust RFC Book](https://rust-lang.github.io/rfcs/3668-async-closures.html)

## Ownership, Move Semantics, and Drop

- [move keyword - Rust std docs](https://doc.rust-lang.org/std/keyword.move.html)
- [Capturing - Rust By Example](https://doc.rust-lang.org/rust-by-example/fn/closures/capture.html)
- [Understanding Ownership - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [What is Ownership? - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [The Stack and the Heap - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#the-stack-and-the-heap)
- [Copy trait - Rust std docs](https://doc.rust-lang.org/std/marker/trait.Copy.html)
- [Clone trait - Rust std docs](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Drop trait - Rust std docs](https://doc.rust-lang.org/std/ops/trait.Drop.html)
- [std::mem::drop - Rust std docs](https://doc.rust-lang.org/std/mem/fn.drop.html)
- [Running Code on Cleanup with the Drop Trait - The Rust Programming Language](https://doc.rust-lang.org/book/ch15-03-drop.html)
- [Destructors - The Rust Reference](https://doc.rust-lang.org/stable/reference/destructors.html)
- [Tail expression temporary scope - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/temporary-tail-expr-scope.html)
- [if let temporary scope - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/temporary-if-let-scope.html)

## Borrowing, References, and Lifetimes

- [References and Borrowing - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [The Slice Type - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [str::find - Rust std docs](https://doc.rust-lang.org/std/primitive.str.html#method.find)
- [Validating References with Lifetimes - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html)
- [Borrowing - Rust By Example](https://doc.rust-lang.org/rust-by-example/scope/borrow.html)
- [Lifetimes - Rust By Example](https://doc.rust-lang.org/rust-by-example/scope/lifetime.html)
- [E0596 Error Code Reference](https://doc.rust-lang.org/error_codes/E0596.html)
- [E0499 Error Code Reference](https://doc.rust-lang.org/error_codes/E0499.html)
- [E0502 Error Code Reference](https://doc.rust-lang.org/error_codes/E0502.html)
- [E0106 Error Code Reference](https://doc.rust-lang.org/error_codes/E0106.html)
- [if let temporary scope - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/temporary-if-let-scope.html)
- [RPIT lifetime capture rules - The Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/rpit-lifetime-capture.html)
- [Match ergonomics reservations - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/match-ergonomics.html)
- [Disallow references to static mut - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/static-mut-references.html)

## Structs, Methods, and Formatting

- [Using Structs to Structure Related Data - The Rust Programming Language](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Defining and Instantiating Structs - The Rust Programming Language](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [An Example Program Using Structs - The Rust Programming Language](https://doc.rust-lang.org/book/ch05-02-example-structs.html)
- [Method Syntax - The Rust Programming Language](https://doc.rust-lang.org/book/ch05-03-method-syntax.html)
- [Debug trait - Rust std docs](https://doc.rust-lang.org/std/fmt/trait.Debug.html)
- [Display trait - Rust std docs](https://doc.rust-lang.org/std/fmt/trait.Display.html)
- [Derive - Rust By Example](https://doc.rust-lang.org/rust-by-example/trait/derive.html)
- [Constructor - Rust Design Patterns](https://rust-unofficial.github.io/patterns/idioms/ctor.html)
- [Match Ergonomics Reservations - Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/match-ergonomics.html)

## Enums, Pattern Matching, and Destructuring

- [Defining an Enum - The Rust Programming Language](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [The match Control Flow Construct - The Rust Programming Language](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Concise Control Flow with if let - The Rust Programming Language](https://doc.rust-lang.org/book/ch06-03-if-let.html)
- [Patterns and Matching - The Rust Programming Language](https://doc.rust-lang.org/book/ch19-00-patterns.html)
- [Pattern Syntax - The Rust Programming Language](https://doc.rust-lang.org/book/ch19-03-pattern-syntax.html)
- [Patterns - The Rust Reference](https://doc.rust-lang.org/reference/patterns.html)
- [E0004 Error Code Reference](https://doc.rust-lang.org/error_codes/E0004.html)
- [Match Ergonomics Reservations - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/match-ergonomics.html)
- [RFC 3627: Match Ergonomics 2024](https://rust-lang.github.io/rfcs/3627-match-ergonomics-2024.html)
- [if let temporary scope - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/temporary-if-let-scope.html)
- [let chains in if and while - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/let-chains.html)
- [Announcing Rust 1.88.0 | Rust Blog](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
- [let-else statements - The Rust Reference](https://doc.rust-lang.org/reference/statements.html#let-else-statements)
- [Announcing Rust 1.65.0 (let-else stabilization) - Rust Blog](https://blog.rust-lang.org/2022/11/03/Rust-1.65.0.html)
- [matches! macro - Rust std docs](https://doc.rust-lang.org/std/macro.matches.html)
- [std::mem::discriminant - Rust std docs](https://doc.rust-lang.org/std/mem/fn.discriminant.html)
- [Box<T> - Rust std docs](https://doc.rust-lang.org/std/boxed/struct.Box.html)

## Option, Result, and Error Handling

- [Option enum - Rust std docs](https://doc.rust-lang.org/std/option/enum.Option.html)
- [Result enum - Rust std docs](https://doc.rust-lang.org/std/result/enum.Result.html)
- [The ? operator - The Rust Reference](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-question-mark-operator)
- [Error Handling - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Recoverable Errors with Result - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [To panic! or Not to panic! - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html)
- [E0369 Error Code Reference](https://doc.rust-lang.org/error_codes/E0369.html)
- [Option::is_some_and - Rust std docs](https://doc.rust-lang.org/std/option/enum.Option.html#method.is_some_and)
- [Option::is_none_or - Rust std docs](https://doc.rust-lang.org/std/option/enum.Option.html#method.is_none_or)
- [Option::flatten - Rust std docs](https://doc.rust-lang.org/std/option/enum.Option.html#method.flatten)
- [Result::flatten - Rust std docs](https://doc.rust-lang.org/std/result/enum.Result.html#method.flatten)
- [Make Illegal States Unrepresentable - corrode.dev](https://corrode.dev/blog/illegal-state/)
- [The Typestate Pattern in Rust - Cliffle](https://cliffle.com/blog/rust-typestate/)
- [E0451 Error Code Reference (private field access)](https://doc.rust-lang.org/error_codes/E0451.html)
- [Visibility and Privacy - The Rust Reference](https://doc.rust-lang.org/reference/visibility-and-privacy.html)

## Traits, Derive, and Conversion Traits

- [Traits: Defining Shared Behavior - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Trait Syntax - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#trait-bound-syntax)
- [Default Implementations - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#default-implementations)
- [Derive - Rust By Example](https://doc.rust-lang.org/rust-by-example/trait/derive.html)
- [Debug trait - Rust std docs](https://doc.rust-lang.org/std/fmt/trait.Debug.html)
- [Display trait - Rust std docs](https://doc.rust-lang.org/std/fmt/trait.Display.html)
- [Clone trait - Rust std docs](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Copy trait - Rust std docs](https://doc.rust-lang.org/std/marker/trait.Copy.html)
- [PartialEq trait - Rust std docs](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- [Eq trait - Rust std docs](https://doc.rust-lang.org/std/cmp/trait.Eq.html)
- [Hash trait - Rust std docs](https://doc.rust-lang.org/std/hash/trait.Hash.html)
- [Default trait - Rust std docs](https://doc.rust-lang.org/std/default/trait.Default.html)
- [PartialOrd trait - Rust std docs](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html)
- [Ord trait - Rust std docs](https://doc.rust-lang.org/std/cmp/trait.Ord.html)
- [From trait - Rust std docs](https://doc.rust-lang.org/std/convert/trait.From.html)
- [Into trait - Rust std docs](https://doc.rust-lang.org/std/convert/trait.Into.html)
- [TryFrom trait - Rust std docs](https://doc.rust-lang.org/std/convert/trait.TryFrom.html)
- [TryInto trait - Rust std docs](https://doc.rust-lang.org/std/convert/trait.TryInto.html)
- [AsRef trait - Rust std docs](https://doc.rust-lang.org/std/convert/trait.AsRef.html)
- [Add trait (std::ops) - Rust std docs](https://doc.rust-lang.org/std/ops/trait.Add.html)
- [Operator Overloading - Rust By Example](https://doc.rust-lang.org/rust-by-example/trait/ops.html)
- [Orphan Rule / Coherence - The Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementation-coherence)
- [fmt::from_fn - Rust std docs](https://doc.rust-lang.org/std/fmt/fn.from_fn.html)
- [fmt::FromFn - Rust std docs](https://doc.rust-lang.org/std/fmt/struct.FromFn.html)
- [Announcing Rust 1.93.0 (fmt::from_fn stabilization) - Rust Blog](https://blog.rust-lang.org/2026/01/22/Rust-1.93.0/)
- [Announcing Rust 1.86.0 (trait upcasting) - Rust Blog](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0/)
- [RFC 3324: dyn Upcasting Coercion - The Rust RFC Book](https://rust-lang.github.io/rfcs/3324-dyn-upcasting.html)

## Supertraits

- [Supertraits - The Rust Programming Language](https://doc.rust-lang.org/book/ch20-02-advanced-traits.html#using-supertraits-to-require-one-traits-functionality-within-another-trait)
- [Supertraits - Rust By Example](https://doc.rust-lang.org/rust-by-example/trait/supertraits.html)
- [Supertraits - The Rust Reference](https://doc.rust-lang.org/reference/items/traits.html#supertraits)

## Generics, Monomorphization, and Trait Objects

- [Generic Data Types - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-01-syntax.html)
- [Traits as Parameters / Trait Bound Syntax - The Rust Programming Language](https://doc.rust-lang.org/book/ch10-02-traits.html#trait-bound-syntax)
- [Advanced Traits (associated types, operator overloading) - The Rust Programming Language](https://doc.rust-lang.org/book/ch20-02-advanced-traits.html)
- [Impl Trait Type - The Rust Reference](https://doc.rust-lang.org/reference/types/impl-trait.html)
- [Trait Objects - The Rust Reference](https://doc.rust-lang.org/reference/types/trait-object.html)
- [Where clauses - Rust By Example](https://doc.rust-lang.org/rust-by-example/generics/where.html)
- [Monomorphization - Rust Compiler Development Guide](https://rustc-dev-guide.rust-lang.org/backend/monomorph.html)
- [RPIT Lifetime Capture Rules 2024 - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/rpit-lifetime-capture.html)
- [Changes to impl Trait in Rust 2024 - Rust Blog](https://blog.rust-lang.org/2024/09/05/impl-trait-capture-rules/)
- [RFC 3498 - Lifetime Capture Rules 2024](https://rust-lang.github.io/rfcs/3498-lifetime-capture-rules-2024.html)
- [RFC 3617 - Precise Capturing (use<> syntax)](https://rust-lang.github.io/rfcs/3617-precise-capturing.html)
- [RFC 3425 - Return Position Impl Trait in Traits](https://rust-lang.github.io/rfcs/3425-return-position-impl-trait-in-traits.html)
- [Announcing async fn and return-position impl Trait in traits - Rust Blog](https://blog.rust-lang.org/2023/12/21/async-fn-rpit-in-traits/)
- [Dyn compatibility rename (lang-team #286)](https://github.com/rust-lang/lang-team/issues/286)
- [Announcing Rust 1.86.0 (trait upcasting, dyn compatible) - Rust Blog](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0/)
- [RFC 2289 - Associated Type Bounds](https://rust-lang.github.io/rfcs/2289-associated-type-bounds.html)
- [Announcing Rust 1.79.0 (associated type bounds stabilization) - Rust Blog](https://blog.rust-lang.org/2024/06/13/Rust-1.79.0/)
- [Const Generics MVP - The Rust Reference](https://doc.rust-lang.org/reference/items/generics.html#const-generics)
- [Const Generics - Rust By Example](https://doc.rust-lang.org/rust-by-example/generics/const_generics.html)
- [Announcing Rust 1.51.0 (const generics MVP stabilization) - Rust Blog](https://blog.rust-lang.org/2021/03/25/Rust-1.51.0/)
- [E0369 Error Code Reference](https://doc.rust-lang.org/error_codes/E0369.html)

## Floating-Point Methods and Ordering

- [f64 primitive type - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html)
- [f64::abs - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.abs)
- [f64::sqrt - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.sqrt)
- [f64::round - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.round)
- [f64::ceil - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.ceil)
- [f64::floor - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.floor)
- [f64::powi - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.powi)
- [f64::clamp - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.clamp)
- [f64::is_nan - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.is_nan)
- [f64::is_infinite - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.is_infinite)
- [f64::is_finite - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.is_finite)
- [f64::round_ties_even - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.round_ties_even)
- [Announcing Rust 1.77.0 (round_ties_even stabilization) - Rust Blog](https://blog.rust-lang.org/2024/03/21/Rust-1.77.0/)
- [IEEE 754 - Wikipedia](https://en.wikipedia.org/wiki/IEEE_754)
- [f64::total_cmp - Rust std docs](https://doc.rust-lang.org/std/primitive.f64.html#method.total_cmp)
- [Announcing Rust 1.62.0 (total_cmp stabilization) - Rust Blog](https://blog.rust-lang.org/2022/06/30/Rust-1.62.0/)
- [std::f64::consts module - Rust std docs](https://doc.rust-lang.org/std/f64/consts/index.html)
- [f64::consts::GOLDEN_RATIO - Rust std docs](https://doc.rust-lang.org/std/f64/consts/constant.GOLDEN_RATIO.html)
- [f64::consts::EULER_GAMMA - Rust std docs](https://doc.rust-lang.org/std/f64/consts/constant.EULER_GAMMA.html)
- [Golden ratio - Wikipedia](https://en.wikipedia.org/wiki/Golden_ratio)
- [Euler-Mascheroni constant - Wikipedia](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant)
- [Tracking Issue #72599: total_cmp for f32 and f64](https://github.com/rust-lang/rust/issues/72599)

## Iterators and Functional Patterns

- [Iterator trait - Rust std docs](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [IntoIterator trait - Rust std docs](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html)
- [std::iter module - Rust std docs](https://doc.rust-lang.org/std/iter/index.html)
- [Iterators - The Rust Programming Language](https://doc.rust-lang.org/book/ch13-02-iterators.html)
- [Processing a Series of Items with Iterators - The Rust Programming Language](https://doc.rust-lang.org/book/ch13-02-iterators.html)
- [Comparing Performance: Loops vs. Iterators - The Rust Programming Language](https://doc.rust-lang.org/book/ch13-04-performance.html)
- [Iterator - Rust By Example](https://doc.rust-lang.org/rust-by-example/trait/iter.html)
- [FromIterator trait - Rust std docs](https://doc.rust-lang.org/std/iter/trait.FromIterator.html)
- [iter::repeat_n - Rust std docs](https://doc.rust-lang.org/std/iter/fn.repeat_n.html)
- [iter::successors - Rust std docs](https://doc.rust-lang.org/std/iter/fn.successors.html)
- [iter::from_fn - Rust std docs](https://doc.rust-lang.org/std/iter/fn.from_fn.html)
- [iter::once - Rust std docs](https://doc.rust-lang.org/std/iter/fn.once.html)
- [Iterator::map_while - Rust std docs](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map_while)
- [Iterator::is_sorted - Rust std docs](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.is_sorted)
- [IntoIterator for Box slice - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/intoiterator-box-slice.html)
- [Announcing Rust 1.82.0 (is_sorted, repeat_n) - Rust Blog](https://blog.rust-lang.org/2024/10/17/Rust-1.82.0/)
- [slice::array_windows - Rust std docs](https://doc.rust-lang.org/std/primitive.slice.html#method.array_windows)
- [slice::windows - Rust std docs](https://doc.rust-lang.org/std/primitive.slice.html#method.windows)
- [Stabilize array_windows - PR #148814](https://github.com/rust-lang/rust/pull/148814)
- [Peekable - Rust std docs](https://doc.rust-lang.org/std/iter/struct.Peekable.html)
- [Peekable::next_if - Rust std docs](https://doc.rust-lang.org/std/iter/struct.Peekable.html#method.next_if)
- [Stabilize peekable_next_if - PR #80011](https://github.com/rust-lang/rust/pull/80011)
- [Peekable::next_if_map - Rust std docs](https://doc.rust-lang.org/std/iter/struct.Peekable.html#method.next_if_map)
- [Tracking Issue for peekable_next_if_map - Issue #143702](https://github.com/rust-lang/rust/issues/143702)
- [Tracking Issue for slice::array_windows - Issue #75027](https://github.com/rust-lang/rust/issues/75027)

## Error Handling in Practice

- [std::error::Error trait - Rust std docs](https://doc.rust-lang.org/std/error/trait.Error.html)
- [core::error::Error trait - Rust std docs](https://doc.rust-lang.org/core/error/trait.Error.html)
- [Announcing Rust 1.81.0 (core::error::Error stabilization) - Rust Blog](https://blog.rust-lang.org/2024/09/05/Rust-1.81.0/)
- [thiserror crate - docs.rs](https://docs.rs/thiserror/latest/thiserror/)
- [thiserror crate - crates.io](https://crates.io/crates/thiserror)
- [thiserror 2.0.0 Release Notes - GitHub](https://github.com/dtolnay/thiserror/releases/tag/2.0.0)
- [anyhow crate - docs.rs](https://docs.rs/anyhow/latest/anyhow/)
- [anyhow crate - crates.io](https://crates.io/crates/anyhow)
- [Error Handling - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Recoverable Errors with Result - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
- [To panic! or Not to panic! - The Rust Programming Language](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html)
- [Result::inspect_err - Rust std docs](https://doc.rust-lang.org/std/result/enum.Result.html#method.inspect_err)
- [Result::inspect - Rust std docs](https://doc.rust-lang.org/std/result/enum.Result.html#method.inspect)
- [Option::inspect - Rust std docs](https://doc.rust-lang.org/std/option/enum.Option.html#method.inspect)
- [std::process::Termination trait - Rust std docs](https://doc.rust-lang.org/std/process/trait.Termination.html)
- [std::process::ExitCode - Rust std docs](https://doc.rust-lang.org/std/process/struct.ExitCode.html)
- [Type Aliases - The Rust Reference](https://doc.rust-lang.org/reference/items/type-aliases.html)
- [std::io::Result type alias - Rust std docs](https://doc.rust-lang.org/std/io/type.Result.html)

## Collections, Strings, and Smart Pointers

- [Vec<T> - Rust std docs](https://doc.rust-lang.org/std/vec/struct.Vec.html)
- [VecDeque<T> - Rust std docs](https://doc.rust-lang.org/std/collections/struct.VecDeque.html)
- [VecDeque::pop_front_if - Rust std docs](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.pop_front_if)
- [std::collections module - when to use each collection](https://doc.rust-lang.org/std/collections/index.html)
- [HashMap<K, V> - Rust std docs](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [HashSet<T> - Rust std docs](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
- [Entry API - Rust std docs](https://doc.rust-lang.org/std/collections/hash_map/enum.Entry.html)
- [BTreeMap<K, V> - Rust std docs](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html)
- [BTreeSet<T> - Rust std docs](https://doc.rust-lang.org/std/collections/struct.BTreeSet.html)
- [BTreeMap::range - Rust std docs](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html#method.range)
- [String - Rust std docs](https://doc.rust-lang.org/std/string/struct.String.html)
- [str (primitive) - Rust std docs](https://doc.rust-lang.org/std/primitive.str.html)
- [Storing UTF-8 Encoded Text with Strings - The Rust Programming Language](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Storing Keys with Associated Values in Hash Maps - The Rust Programming Language](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)
- [Common Collections - The Rust Programming Language](https://doc.rust-lang.org/book/ch08-00-common-collections.html)
- [Box<T> - Rust std docs](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Using Box to Point to Data on the Heap - The Rust Programming Language](https://doc.rust-lang.org/book/ch15-01-box.html)
- [Rc<T> - Rust std docs](https://doc.rust-lang.org/std/rc/struct.Rc.html)
- [Reference Counted Smart Pointer - The Rust Programming Language](https://doc.rust-lang.org/book/ch15-04-rc.html)
- [Arc<T> - Rust std docs](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [Shared-State Concurrency - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-03-shared-state.html)
- [Use borrowed types for arguments - Rust Design Patterns](https://rust-unofficial.github.io/patterns/idioms/coercion-arguments.html)
- [Clone to satisfy the borrow checker (anti-pattern) - Rust Design Patterns](https://rust-unofficial.github.io/patterns/anti_patterns/borrow_clone.html)
- [The Rust Performance Book: Heap Allocations](https://nnethercote.github.io/perf-book/heap-allocations.html)
- [IntoIterator for Box slice - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/intoiterator-box-slice.html)
- [slice::get_disjoint_mut - Rust std docs](https://doc.rust-lang.org/std/primitive.slice.html#method.get_disjoint_mut)
- [Announcing Rust 1.86.0 (get_disjoint_mut) - Rust Blog](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0/)
- [Vec::extract_if - Rust std docs](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.extract_if)
- [HashMap::extract_if - Rust std docs](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.extract_if)
- [Announcing Rust 1.87.0 (Vec::extract_if) - Rust Blog](https://blog.rust-lang.org/2025/05/15/Rust-1.87.0/)
- [Announcing Rust 1.88.0 (HashMap::extract_if) - Rust Blog](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
- [str::floor_char_boundary - Rust std docs](https://doc.rust-lang.org/std/primitive.str.html#method.floor_char_boundary)
- [str::ceil_char_boundary - Rust std docs](https://doc.rust-lang.org/std/primitive.str.html#method.ceil_char_boundary)
- [Announcing Rust 1.91.0 (floor/ceil_char_boundary) - Rust Blog](https://blog.rust-lang.org/2025/10/30/Rust-1.91.0/)
- [Vec::pop_if - Rust std docs](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.pop_if)
- [Announcing Rust 1.86.0 (Vec::pop_if) - Rust Blog](https://blog.rust-lang.org/2025/04/03/Rust-1.86.0/)
- [slice::as_array - Rust std docs](https://doc.rust-lang.org/std/primitive.slice.html#method.as_array)
- [Announcing Rust 1.93.0 (as_array stabilization) - Rust Blog](https://blog.rust-lang.org/2026/01/22/Rust-1.93.0/)
- [slice::as_chunks - Rust std docs](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks)
- [Announcing Rust 1.88.0 (as_chunks stabilization) - Rust Blog](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
- [Cell<T> - Rust std docs](https://doc.rust-lang.org/std/cell/struct.Cell.html)
- [Cell::update - Rust std docs](https://doc.rust-lang.org/std/cell/struct.Cell.html#method.update) — stabilized Rust 1.88.0
- [RefCell<T> - Rust std docs](https://doc.rust-lang.org/std/cell/struct.RefCell.html)
- [Cow<T> - Rust std docs](https://doc.rust-lang.org/std/borrow/enum.Cow.html)
- [String::from_utf8_lossy - Rust std docs](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy)
- [Clone on write (Cow) - Rust Design Patterns](https://rust-unofficial.github.io/patterns/idioms/cow.html)
- [Slice Patterns - The Rust Reference](https://doc.rust-lang.org/reference/patterns.html#slice-patterns)
- [RFC 2359: Subslice Pattern Syntax](https://rust-lang.github.io/rfcs/2359-subslice-pattern-syntax.html)
- [Destructuring Slices/Arrays - Rust by Example](https://doc.rust-lang.org/rust-by-example/flow_control/match/destructuring/destructure_slice.html)

## Modules, Visibility, and Project Structure

- [Managing Growing Projects with Packages, Crates, and Modules - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html)
- [Separating Modules into Different Files - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-05-separating-modules-into-different-files.html)
- [Defining Modules to Control Scope and Privacy - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)
- [Paths for Referring to an Item in the Module Tree - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html)
- [Bringing Paths into Scope with the use Keyword - The Rust Programming Language](https://doc.rust-lang.org/book/ch07-04-bringing-names-into-scope-with-the-use-keyword.html)
- [Modules - The Rust Reference](https://doc.rust-lang.org/reference/items/modules.html)
- [Visibility and Privacy - The Rust Reference](https://doc.rust-lang.org/reference/visibility-and-privacy.html)
- [Package Layout - The Cargo Book](https://doc.rust-lang.org/cargo/guide/project-layout.html)
- [The Manifest Format - The Cargo Book](https://doc.rust-lang.org/cargo/reference/manifest.html)
- [Workspaces - The Cargo Book](https://doc.rust-lang.org/cargo/reference/workspaces.html)
- [Specifying Dependencies - The Cargo Book](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Cargo: Rust-version aware resolver - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/cargo-resolver.html)
- [Cargo: Reject unused inherited default-features - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/cargo-inherited-default-features.html)
- [gen keyword - The Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/gen-keyword.html)
- [RFC 3389: Manifest Lints - The Rust RFC Book](https://rust-lang.github.io/rfcs/3389-manifest-lint.html)
- [RFC 2906: Workspace Dependency Deduplication - The Rust RFC Book](https://rust-lang.github.io/rfcs/2906-cargo-workspace-deduplicate.html)
- [Minimize Visibility - Effective Rust](https://effective-rust.com/visibility.html)
- [Announcing Rust 1.88.0 | Rust Blog](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/) — Cargo automatic cache garbage collection
- [Cargo Cache Cleaning | Rust Blog](https://blog.rust-lang.org/2023/12/11/cargo-cache-cleaning/) — design overview
- [Stabilize automatic garbage collection - cargo PR #14287](https://github.com/rust-lang/cargo/pull/14287)
- [Configuration - The Cargo Book](https://doc.rust-lang.org/cargo/reference/config.html) — `[cache]` section
- [RFC 2383: Lint Reasons - The Rust RFC Book](https://rust-lang.github.io/rfcs/2383-lint-reasons.html) — `#[expect]` attribute
- [Lint levels - The rustc book](https://doc.rust-lang.org/rustc/lints/levels.html#expecting-lints) — expect vs allow

## Testing

- [How to Write Tests - The Rust Programming Language](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [Controlling How Tests Are Run - The Rust Programming Language](https://doc.rust-lang.org/book/ch11-02-running-tests.html)
- [Test Organization - The Rust Programming Language](https://doc.rust-lang.org/book/ch11-03-test-organization.html)
- [Documentation Tests - The rustdoc book](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
- [cargo test - The Cargo Book](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [Unit testing - Rust By Example](https://doc.rust-lang.org/rust-by-example/testing/unit_testing.html)
- [Integration testing - Rust By Example](https://doc.rust-lang.org/rust-by-example/testing/integration_testing.html)
- [Doc testing - Rust By Example](https://doc.rust-lang.org/rust-by-example/testing/doc_testing.html)
- [Rustdoc Combined Doctests - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/rustdoc-doctests.html)
- [assert! macro - Rust std docs](https://doc.rust-lang.org/std/macro.assert.html)
- [assert_eq! macro - Rust std docs](https://doc.rust-lang.org/std/macro.assert_eq.html)
- [assert_ne! macro - Rust std docs](https://doc.rust-lang.org/std/macro.assert_ne.html)
- [Announcing Rust 1.89.0 (doctest cross-compilation) - Rust Blog](https://blog.rust-lang.org/2025/08/07/Rust-1.89.0/)

## Documentation Generation

- [cargo doc - The Cargo Book](https://doc.rust-lang.org/cargo/commands/cargo-doc.html)
- [How to Write Documentation - The rustdoc book](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- [The #[doc] attribute - The rustdoc book](https://doc.rust-lang.org/rustdoc/write-documentation/the-doc-attribute.html)
- [What to include (and exclude) - The rustdoc book](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)

## Concurrency, Threads, and Synchronization

- [std::thread module - Rust std docs](https://doc.rust-lang.org/std/thread/)
- [thread::spawn - Rust std docs](https://doc.rust-lang.org/std/thread/fn.spawn.html)
- [thread::scope - Rust std docs](https://doc.rust-lang.org/std/thread/fn.scope.html)
- [thread::available_parallelism - Rust std docs](https://doc.rust-lang.org/std/thread/fn.available_parallelism.html)
- [JoinHandle - Rust std docs](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html)
- [Send trait - Rust std docs](https://doc.rust-lang.org/std/marker/trait.Send.html)
- [Sync trait - Rust std docs](https://doc.rust-lang.org/std/marker/trait.Sync.html)
- [Send and Sync - The Rustonomicon](https://doc.rust-lang.org/nomicon/send-and-sync.html)
- [Mutex - Rust std docs](https://doc.rust-lang.org/std/sync/struct.Mutex.html)
- [Arc - Rust std docs](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [std::sync::mpsc - Rust std docs](https://doc.rust-lang.org/std/sync/mpsc/index.html)
- [Fearless Concurrency - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
- [Using Threads to Run Code Simultaneously - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-01-threads.html)
- [Using Message Passing to Transfer Data Between Threads - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-02-message-passing.html)
- [Shared-State Concurrency - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-03-shared-state.html)
- [Extensible Concurrency with Send and Sync - The Rust Programming Language](https://doc.rust-lang.org/book/ch16-04-extensible-concurrency-sync-and-send.html)
- [RwLock - Rust std docs](https://doc.rust-lang.org/std/sync/struct.RwLock.html)
- [RwLockWriteGuard::downgrade - Rust std docs](https://doc.rust-lang.org/std/sync/struct.RwLockWriteGuard.html#method.downgrade)
- [std::sync::atomic module - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/index.html)
- [AtomicBool - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html)
- [AtomicUsize - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html)
- [Ordering - Rust std docs](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html)
- [Announcing Rust 1.92.0 - Rust Blog](https://blog.rust-lang.org/2025/12/11/Rust-1.92.0/)
- [Why Rust mutexes look like they do - Cliffle](https://cliffle.com/blog/rust-mutexes/)
- [std::io::pipe - Rust std docs](https://doc.rust-lang.org/std/io/fn.pipe.html)
- [PipeReader - Rust std docs](https://doc.rust-lang.org/std/io/struct.PipeReader.html)
- [PipeWriter - Rust std docs](https://doc.rust-lang.org/std/io/struct.PipeWriter.html)
- [Announcing Rust 1.87.0 - Rust Blog](https://blog.rust-lang.org/2025/05/15/Rust-1.87.0/)
- [File::lock - Rust std docs](https://doc.rust-lang.org/std/fs/struct.File.html#method.lock)
- [File::try_lock - Rust std docs](https://doc.rust-lang.org/std/fs/struct.File.html#method.try_lock)
- [File::lock_shared - Rust std docs](https://doc.rust-lang.org/std/fs/struct.File.html#method.lock_shared)
- [TryLockError - Rust std docs](https://doc.rust-lang.org/std/fs/enum.TryLockError.html)
- [Tracking Issue for File lock API - #130994](https://github.com/rust-lang/rust/issues/130994)
- [Announcing Rust 1.89.0 (File::lock stabilization) - Rust Blog](https://blog.rust-lang.org/2025/08/07/Rust-1.89.0/)

## Async, Futures, and Runtimes

- [Future trait - Rust std docs](https://doc.rust-lang.org/std/future/trait.Future.html)
- [The Future Trait - Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/02_execution/02_future.html)
- [Async in depth - Tokio Tutorial](https://tokio.rs/tokio/tutorial/async)
- [Spawning - Tokio Tutorial](https://tokio.rs/tokio/tutorial/spawning)
- [RFC 3668 - Async Closures](https://rust-lang.github.io/rfcs/3668-async-closures.html)
- [Stabilize async closures (PR #132706)](https://github.com/rust-lang/rust/pull/132706)
- [AsyncFn trait - Rust std docs](https://doc.rust-lang.org/stable/std/ops/trait.AsyncFn.html)
- [AsyncFnMut trait - Rust std docs](https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnMut.html)
- [AsyncFnOnce trait - Rust std docs](https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnOnce.html)
- [Gate async Fn() bound modifier on async_trait_bounds (PR #132612)](https://github.com/rust-lang/rust/pull/132612)
- [Async Closures MVP: Call for Testing - Inside Rust Blog](https://blog.rust-lang.org/inside-rust/2024/08/09/async-closures-call-for-testing/)
- [Newly Unsafe Functions - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/newly-unsafe-functions.html)
- [Unsafe extern blocks - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html)

## Idiomatic Patterns

- [Builder Pattern - Rust Design Patterns (Unofficial)](https://rust-unofficial.github.io/patterns/patterns/creational/builder.html)
- [Item 7: Use builders for complex types - Effective Rust](https://effective-rust.com/builders.html)
- [The Typestate Pattern in Rust - Cliffle](https://cliffle.com/blog/rust-typestate/)
- [Typestate Programming - The Embedded Rust Book](https://docs.rust-embedded.org/book/static-guarantees/typestate-programming.html)
- [Type-Driven API Design in Rust: Typestate - Will Crichton](https://willcrichton.net/rust-api-type-patterns/typestate.html)
- [PhantomData - Rust std docs](https://doc.rust-lang.org/std/marker/struct.PhantomData.html)
- [RFC 0445 - Extension Trait Conventions](https://rust-lang.github.io/rfcs/0445-extension-trait-conventions.html)
- [Extension Traits, Greppability and IDEs - Eli Bendersky](https://eli.thegreenplace.net/2022/rust-extension-traits-greppability-and-ides/)
- [Rust API Guidelines: Future Proofing (C-SEALED)](https://rust-lang.github.io/api-guidelines/future-proofing.html)
- [Newtype Pattern - Rust Design Patterns](https://rust-unofficial.github.io/patterns/patterns/behavioural/newtype.html)
- [std::process::Command (borrowing builder example) - Rust std docs](https://doc.rust-lang.org/std/process/struct.Command.html)
- [Itertools trait - docs.rs](https://docs.rs/itertools/latest/itertools/trait.Itertools.html)

## Anti-Patterns and Common Mistakes

- [Anti-Patterns Catalogue - Rust Design Patterns](https://rust-unofficial.github.io/patterns/anti_patterns/)
- [Clone to Satisfy the Borrow Checker - Rust Design Patterns](https://rust-unofficial.github.io/patterns/anti_patterns/borrow_clone.html)
- [Deref Polymorphism Anti-Pattern - Rust Design Patterns](https://rust-unofficial.github.io/patterns/anti_patterns/deref.html)
- [#[deny(warnings)] Anti-Pattern - Rust Design Patterns](https://rust-unofficial.github.io/patterns/anti_patterns/deny-warnings.html)
- [Using unwrap() in Rust is Okay - Andrew Gallant (BurntSushi)](https://burntsushi.net/unwrap/)
- [Rust API Guidelines: Naming](https://rust-lang.github.io/api-guidelines/naming.html)
- [Rust API Guidelines: Type Safety](https://rust-lang.github.io/api-guidelines/type-safety.html)
- [Item 6: Embrace the Newtype Pattern - Effective Rust](https://www.lurklurk.org/effective-rust/newtype.html)
- [Item 9: Iterator Transforms Instead of Explicit Loops - Effective Rust](https://effective-rust.com/iterators.html)
- [Pitfalls of Safe Rust - corrode.dev](https://corrode.dev/blog/pitfalls-of-safe-rust/)
- [Patterns for Defensive Programming in Rust - corrode.dev](https://corrode.dev/blog/defensive-programming/)
- [Unsafe Rust in the Wild - Rust Foundation (2024)](https://rustfoundation.org/media/unsafe-rust-in-the-wild-notes-on-the-current-state-of-unsafe-rust/)
- [safety-dance: Auditing Crates for Replaceable Unsafe Code](https://github.com/rust-secure-code/safety-dance)
- [unsafe_op_in_unsafe_fn - The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-op-in-unsafe-fn.html)
- [Comparing Performance: Loops vs. Iterators - The Rust Programming Language](https://doc.rust-lang.org/book/ch13-04-performance.html)
- [Use Borrowed Types for Arguments - Rust Design Patterns](https://rust-unofficial.github.io/patterns/idioms/coercion-arguments.html)

## Where to Go from Here (Async, Unsafe 2024, Macros, Ecosystem)

- [Asynchronous Programming in Rust (async book)](https://rust-lang.github.io/async-book/)
- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)
- [tokio crate - docs.rs](https://docs.rs/tokio/latest/tokio/)
- [JoinSet in tokio::task - docs.rs](https://docs.rs/tokio/latest/tokio/task/struct.JoinSet.html)
- [Announcing async fn and return-position impl Trait in traits - Rust Blog](https://blog.rust-lang.org/2023/12/21/async-fn-rpit-in-traits/)
- [RFC 3668 - Async Closures](https://rust-lang.github.io/rfcs/3668-async-closures.html)
- [The State of Async Rust: Runtimes - corrode.dev](https://corrode.dev/blog/async/)
- [The Rustonomicon - Unsafe Rust](https://doc.rust-lang.org/nomicon/)
- [unsafe_op_in_unsafe_fn - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-op-in-unsafe-fn.html)
- [Unsafe extern blocks - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html)
- [Disallow references to static mut - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/static-mut-references.html)
- [Newly unsafe functions - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/newly-unsafe-functions.html)
- [Unsafe attributes - Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-attributes.html)
- [Macros - The Rust Reference](https://doc.rust-lang.org/reference/macros.html)
- [Procedural Macros - The Rust Reference](https://doc.rust-lang.org/reference/procedural-macros.html)
- [The Little Book of Rust Macros](https://veykril.github.io/tlborm/)
- [Declarative macro improvements - Rust Project Goals 2025H1](https://rust-lang.github.io/rust-project-goals/2025h1/macro-improvements.html)
- [syn crate - docs.rs](https://docs.rs/syn/latest/syn/)
- [quote crate - docs.rs](https://docs.rs/quote/latest/quote/)
- [proc-macro2 crate - crates.io](https://crates.io/crates/proc-macro2)
- [axum crate - docs.rs](https://docs.rs/axum/latest/axum/)
- [Announcing axum 0.8.0 - Tokio Blog](https://tokio.rs/blog/2025-01-01-announcing-axum-0-8-0)
- [actix-web crate - docs.rs](https://docs.rs/actix-web/latest/actix_web/)
- [reqwest crate - docs.rs](https://docs.rs/reqwest/latest/reqwest/)
- [hyper crate - docs.rs](https://docs.rs/hyper/latest/hyper/)
- [tonic crate - docs.rs](https://docs.rs/tonic/latest/tonic/)
- [tower crate - docs.rs](https://docs.rs/tower/latest/tower/)
- [clap crate - docs.rs](https://docs.rs/clap/latest/clap/)
- [serde crate - docs.rs](https://docs.rs/serde/latest/serde/)
- [sqlx crate - docs.rs](https://docs.rs/sqlx/latest/sqlx/)
- [diesel crate - docs.rs](https://docs.rs/diesel/latest/diesel/)
- [sea-orm crate - docs.rs](https://docs.rs/sea-orm/latest/sea_orm/)
- [tracing crate - docs.rs](https://docs.rs/tracing/latest/tracing/)
- [embedded-hal 1.0 announcement - Rust Embedded Blog](https://blog.rust-embedded.org/embedded-hal-v1/)
- [esp-hal 1.0.0 release - Espressif](https://developer.espressif.com/blog/2025/10/esp-hal-1/)
- [Embassy - Async Embedded Framework](https://embassy.dev/)
- [wasm-bindgen - docs.rs](https://docs.rs/wasm-bindgen/latest/wasm_bindgen/)
- [Leptos crate - docs.rs](https://docs.rs/leptos/latest/leptos/)
- [Dioxus crate - docs.rs](https://docs.rs/dioxus/latest/dioxus/)
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
- [Effective Rust](https://effective-rust.com/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Rust Performance Book](https://nnethercote.github.io/perf-book/)
- [Rustlings](https://rustlings.rust-lang.org/)
- [Exercism Rust Track](https://exercism.org/tracks/rust)
- [This Week in Rust](https://this-week-in-rust.org/)

## The must_use Attribute

- [Diagnostics: must_use - The Rust Reference](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-must_use-attribute)
- [RFC 1940: must-use functions](https://rust-lang.github.io/rfcs/1940-must-use-functions.html)
- [When to add #[must_use] - Standard Library Developer Guide](https://std-dev-guide.rust-lang.org/policy/must-use.html)
- [unused_must_use - Warn-by-default Lints (rustc book)](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-must-use)

## Community and Analysis

- [Rust 2024 Edition Reaches Stability - Rust Bytes](https://weeklyrust.substack.com/p/rust-2024-edition-reaches-stability)
- [Rust edition 2024 annotated | bertptrs.nl](https://bertptrs.nl/2025/02/23/rust-edition-2024-annotated.html)
