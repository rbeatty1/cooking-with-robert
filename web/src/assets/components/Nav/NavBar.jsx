import { Component } from "react";
import { Link } from "react-router-dom";
import {ROUTE_MAP} from '../../routes/routes.jsx';
import './NavBar.less';

class NavBar extends Component{
    constructor(props){
        super(props);
        this.props = props;
        this.pages = ROUTE_MAP;
    }

    render(){
        return (
            <nav id="nav-bar">
                {Object.keys(this.pages).map( r => <Link className={this.pages[r] === this.props.page ? "active" : "inactive"} to={this.pages[r]}>{this.pages[r].toUpperCase()}</Link>)}
            </nav>
        )
    }
}

export default NavBar;