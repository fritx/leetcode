let calc = (t, n) => {
  return 1
}

let cases = [
  [1, 1, 1],
]
for (let [a, b, c] of cases) {
  console.log([a, b, c, calc(a, b)])
}

let App = () => {
  return (
    <div style={{ padding: 20 }}>
      <h1>Hello world</h1>
      <div style={{ marginTop: 20 }}>
        Here is some content...
      </div>
    </div>
  )
}
