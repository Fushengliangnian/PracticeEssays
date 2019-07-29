import React from 'react'
import ReactDOM from 'react-dom'

const divVD = React.createElement('div', {
    title: 'hello react'
}, 'Hello React！！！');

ReactDOM.render(divVD, document.getElementById('app'));