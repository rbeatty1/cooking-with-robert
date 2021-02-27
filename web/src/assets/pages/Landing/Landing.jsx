import React, {Component} from 'react';
import { ROUTE_MAP } from '../../routes/routes';
import {Link} from 'react-router-dom';
import Button from '../../components/Button/Button';
class Landing extends Component{
    constructor(props){
        super(props);
        this.pages = ROUTE_MAP;
    }
    render(){
        return(
            <div id="landing-page">
                <h1 style={ { textAlign : 'center'}}>BBEATZ</h1>
                <div className="flex_container flex_space-evenly">
                    {
                    Object
                        .keys(this.pages)
                        .map( (r,i) => {
                            return (<Link to={this.pages[r]}><Button label={this.pages[r].toUpperCase()}/></Link>)
                        })
                    }
                </div>
            </div>
        )
    }
}

export default Landing;