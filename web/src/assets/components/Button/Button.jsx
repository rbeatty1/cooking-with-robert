import { Component } from "react";

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
            >
                {this.props.label}
            </button>
        )
    }
}

export default Button;