import NavBar from "../../components/Nav/NavBar";
import './ComingSoon.scss'

const ComingSoon = props =>{
    console.log(props);
    return (
        <div id="coming-soon-page">
            <NavBar page={props.location.pathname.split("/")[1]}></NavBar>
            <h1 style={ {textAlign: "center", marginTop : '5rem'}}>Coming Soon!</h1>
        </div>
    )
}

export default ComingSoon;