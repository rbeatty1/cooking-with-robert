import { Component } from "react";
import './Cards.scss';

class Card extends Component{
    constructor(props){
        super(props)
        this.props = props;
    }

    render(){
        return(this.props.renderFn(this.props.data))
    }
}

class MdCard extends Card{
    constructor(props){
        super(props);
        this.props = props;
    }

    render(){
        return(
            <div key={this.props.id} className="card-wrapper md">
                {this.props.children}
            </div>
        )
    }
}

export {
    MdCard,
    Card
}