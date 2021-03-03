import { Component } from "react";
import "./Button.scss"
class Button extends Component{
    constructor(props){
        super(props);
        this.props = props;
    }

    render(){
        return (
            <button
                type="button"
                onclick={this.props.onclick}
                className="btn main"
            >
                {this.props.label}
            </button>
        )
    }
}

export default Button;