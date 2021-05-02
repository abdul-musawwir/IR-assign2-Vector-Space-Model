// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';

function App(){
  // constructor(props) {
  //   super(props);
  //   // this.md = new Remarkable();
  //   this.handleChange = this.handleChange.bind(this);
  //   this.state = { value: "" };
  // }

  const [query,setQuery] = useState();

  function handletextChange(e){
    setQuery(e.target.value);
    // console.log(query);
  }

  function handleSubmit(){
    console.log(query)
  }

  // getRawMarkup() {
  //   return { __html: this.md.render(this.state.value) };
  // }


  return (
    <div className="Container" >
      <div className="info">
      <p style = {{fontSize:35}}>Abdul Musawwir</p>
      <p style = {{fontSize:35}}>18k-0185</p>
      </div>
      <div className="info2">
        <p className = "mylabel">
          Enter Your query
        </p>
        <br/>
        <div>
        <input className="query"
          onChange={(val) => handletextChange(val)}
        />
        </div>
      </div>
      <div className="info2">
      <h3>Output</h3>
      <p >{query}hello</p>
      </div>
      {/* <div
        className="content"
        // dangerouslySetInnerHTML={this.getRawMarkup()}
      />
      {this.state.value} */}
    </div>
  );
}

export default App;
