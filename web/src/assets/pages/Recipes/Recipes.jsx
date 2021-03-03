import {Component} from 'react';
import { MdCard } from '../../components/Cards/Cards';
import CardContainer from '../../components/Containers/CardContainer/CardContainer';
import NavBar from '../../components/Nav/NavBar';
class Recipes extends Component{
    constructor(props){
        super(props);
        this.props = props;
        this.state = {
            loading : true,
            data : null
        }
    }

    componentDidMount(){
        const recipeQuery = `
        query {
            recipes{
                id
                name
                mealType
                servings
            }
        }
        `

        fetch(
            'http://localhost:8000/graphql/',
            {
                method : 'POST',
                headers : { 'Content-Type' : 'application/json'},
                body : JSON.stringify({ query: recipeQuery })
            }
        )
        .then( res => res.json())
        .then( data =>{
            console.log(data);
            this.setState( { loading : false, data : data.data.recipes })
        }
        )
        .catch( err => alert(err) )
    }

    render(){
        const CreateRecipeCardContent = recipeInfo=>{
            return(
                <div>
                    <h3>{recipeInfo.name}</h3>
                    <h5>{`Servings : ${recipeInfo.servings}`}</h5>
                </div>
            )
        }
        return (
            <div id="recipes-page">
                <NavBar page="recipes"/>
                {
                    this.state.loading ? 
                        <h1>LOADING</h1> : 
                        <CardContainer background="dark">
                            {this.state.data.map((x,i) => <MdCard id={i}>{CreateRecipeCardContent(x)}</MdCard>)}
                        </CardContainer>
                }
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