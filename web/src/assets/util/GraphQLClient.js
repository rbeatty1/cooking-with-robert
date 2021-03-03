import { Client, defaultExchanges, dedupExchange, fetchExchange, cacheExchange } from 'urql'

const cache = cacheExchange({});
const client = new Client(
    {
        url : 'http://localhost:8000/graphql',
        exchanges : defaultExchanges
    }
)

export default client;