import { Component } from "react";
import './CardContainer.scss'

class CardContainer extends Component{
    constructor(props){
        super(props);
        this.props = props;
    }

    render(){
        return( 
        <div 
            className={`card-container ${this.props.background}`}
        >
            {this.props.children}
        </div>
        )
    }
}

export default CardContainer;