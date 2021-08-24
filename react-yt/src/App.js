import './App.css';
function App() {
  function loadVideos(){
    console.log('load videos');
  }
  return (
    <div className="App">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
      <header className="App-header">
        <div>Enter search</div>
        <form method = "post">
        <input type="text" placeholder="Youtube search" name="youtube" id="complete"/>  
        <p>My token = {window.token}</p>
        <br></br>
        <button type='submit' class="btn btn-primary">Search</button>
        </form>
      </header>
    </div>
  );
}
export default App;
