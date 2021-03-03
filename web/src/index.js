import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'urql';
import App from './assets/app.jsx';
import client from './assets/util/GraphQLClient.js';
import './index.scss';

ReactDOM.render(
    <Provider value={client}>
        <App/>
    </Provider>,
    document.getElementById('root')
)