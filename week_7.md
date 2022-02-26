class: center, middle

# MPCS 52553: Web Development
## Week 7: Intro to React
---

class: agenda

# Final Project: Belay

# Intro to React
- Components
- JSX
- Props
- State

---

# Belay: a Slack clone
https://mit.cs.uchicago.edu/trevoraustin/mpcs-52553-austin/tree/master/final_project

For the final project, we'll put together the concepts we've learned this
quarter into a single web application.
* Multi-column and responsive layouts
* Storing and retrieving records from a database
* APIs and asynchronous requests
* Single-page applications

The final project is worth 4 times as much as a regular Exercise and 40% of
your grade overall. You have the remainder of the quarter (i.e. until our last
class on August 26) to complete it.
---

# Introduction to React

You will have noticed in working on Exercise 6 that it can be tedious and
difficult when writing a single-page application to manage what **state** the
app is supposed to be in what elements should be displayed to the user. You have
to change the navigation bar, update variables, and show/hide page elements all
manually, and trigger updates after each API callback.

[React](https://reactjs.org/) is a framework for developing interactive web
pages, and especially single-page applications, developed and released as open
source by Facebook. The powerful thing about it (and competing frameworks like
[Vue](https://vuejs.org/) and [Svelte](https://svelte.dev/)) is it lets you
define how the page should look in various states, and when you update the
state, the framework updates the page automatically for you.

That's less work for you as a developer, and fewer opportunities to make
mistakes.
---

# Why React?

It's the most widely-used front-end framework, and well-liked by those who have
used it. Stats from [State of JS](https://2020.stateofjs.com/en-US/technologies/front-end-frameworks/):

![Front-End Frameworks Usage Chart](images/frontend-frameworks.png)
---


# Lab: React Tic Tac Toe

While React is useful and popular, the docs are OK at best. The best
introduction is the [tutorial](https://reactjs.org/tutorial/tutorial.html), but
even then it has a lot of moving parts. For reasons we'll get into, React relies
on pre-processing the code you write, which requires running [Node](https://nodejs.org/en/),
a separate framework that's for running for server-side Javascript code.

Instead of all that, I've followed the instructions in their low-overhead guide
to [add React to a website](https://reactjs.org/docs/add-react-to-a-website.html)
to make a starter project
[on the class GitLab](https://mit.cs.uchicago.edu/mpcs52553-sum-21/course/tree/master/week_7/examples).
We'll start there and work through the tutorial with it.

We'll be building a simple Tic Tac Toe game like this one:
https://codepen.io/gaearon/pen/gWWZgR?editors=0010
---

# Lab: React Tic Tac Toe

We'll need a local server to host our React application. Navigate to the
`examples` directory for Week 7 and run:

`python3 -m http.server`

That will let you see your Tic Tac Toe application at `http://localhost:8000/tictactoe.html`

From here we'll be working through the instructions on the tutorial in the React
documentation: https://reactjs.org/tutorial/tutorial.html
---

# Lab: React Tic Tac Toe

### Components
- OOP classes that can be re-used
- Takes in parameters called `props`
- Describes what to display in its `render` method

### JSX
- DSL
- Shorthand for `React.createElement(...`
- Evaluates Javascript inside curly braces `{}`
- Can include custom React components in addition to base HTML types
---

# Lab: React Tic Tac Toe

### Props
- Calls a component's `render` method any time they change
- Read-only to support one-directional data flow:
  https://medium.com/@lizdenhup/understanding-unidirectional-data-flow-in-react-3e3524c09d8e
- Can add type checking with [prop-types](https://www.npmjs.com/package/prop-types)

### State
- Update with `this.setState()`
- When you call setState in a component, React automatically updates the child
  components inside of it too.
- To let child components modify state, pass a handler function down to them as
  one of their `props`.
