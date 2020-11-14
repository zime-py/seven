import React, { Component } from 'react';
import axios from 'axios'; // new
class App extends Component {
//default
state = { 
//app1 is app name 
app1: [] 
};
// new
componentDidMount() {
//cool is model name
this.getcool();  
}
// new
getcool() {
axios
//rest api page link
.get('http://127.0.0.1:8000/api/')   
//jason api page link
//.get('http://127.0.0.1:8000/api/?format=json')  
.then(res => {
this.setState({app1: res.data });
})
.catch(err => {
console.log(err);
});
}
render() {
return (
  <div>
{this.state.app1.map(item => (
//default dite hobe
<div key={item.id}> 
<h3>{item.name}</h3>  
</div>
))}
</div>
);
}
}
export default App;