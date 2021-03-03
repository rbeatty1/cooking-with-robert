import React, {Component} from 'react';
import { ROUTE_MAP } from '../../routes/routes';
import {Link} from 'react-router-dom';
import Button from '../../components/Button/Button';
import "./Landing.scss";
class Landing extends Component{
    constructor(props){
        super(props);
        this.pages = ROUTE_MAP;
    }
    render(){
        return(
            <div id="landing-page" className="full-width full-height">
                <h1 style={ { textAlign : 'center'}}>BB<span className="landing_header_emphasis">EATZ</span></h1>
                <div className="flex_container flex_space-evenly lg-width">
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