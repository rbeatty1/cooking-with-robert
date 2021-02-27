import {Component} from 'react';
import NavBar from '../../components/Nav/NavBar';
class Recipes extends Component{
    constructor(props){
        super(props);
        this.props = props;
    }

    render(){
        return (
            <div id="recipes-page">
                <NavBar page="recipes"/>
                <h1>RECIPES PAGE</h1>
            </div>
            /*
                NAV BAR
                FILTERS
                RECIPE CARDS => HIT GRAPHQL
            */
        )
    }
}

export default Recipes;