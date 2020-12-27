class Data:
    def __init__(self):
        self.index_html = '''
        {%load static%}
        <html lang="en">
            <body>
                <div id="root"></div>
            </body>
            <script src = "{% static '/dist/app.bundle.js' %}"></script>
        </html>
        '''.strip()
        self.index_css = '''
        '''
        self.index_js = '''
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import './index.css'
ReactDOM.render(
            <App />,
            document.getElementById('root')
);
        '''.strip()
        self.app_js = '''
import React from 'react';
import './App.css';
import Dact from './dact.svg';

const App = () => {
return(
        <div className="App">
            <Dact className="Applogo"/>
            <div className="Apptext">
                <br></br>    
                <h4>It's Up and Running !!!</h4>
                <h6>
                    <p>
                    Edit App.js to get started with frontend!!
                    </p>
                    <p>
                    Server Running at 127.0.0.1:8000
                    </p>
                    <p>
                        Run dact-watch in BASE_DIR to start dev mode
                    </p>
                </h6>
            </div>
        </div>
        );
}
export default App;
        '''.strip()
        self.app_css = '''
.App
{
    text-align: center;
    color:black;
}
.Applogo
{
    max-width: 100%;
    height: 50%;
    width: 90%; 
}
.Apptext
{
    font-family: sans-serif;
    color:#169A9A;
}
        '''.strip()
        self.dact_svg = '''
<svg width="500" height="700" viewBox="0 0 1152 700" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="500" height="700" fill="#E5E5E5"/>
<rect width="500" height="700" fill="white"/>
<path d="M207.078 307C192.828 301.938 178.016 299.406 162.641 299.406C126.359 299.406 108.219 318.016 108.219 355.234C108.219 398.266 126.359 419.781 162.641 419.781C178.016 419.781 192.828 417.953 207.078 414.297V307ZM221.844 424.141C205.812 430.047 185.609 433 161.234 433C115.391 433 92.4688 407.406 92.4688 356.219C92.4688 308.969 115.812 285.344 162.5 285.344C177.125 285.344 191.984 287.688 207.078 292.375V231.906H221.844V424.141ZM258.406 391.234C258.406 361.891 277.906 347.219 316.906 347.219C330.688 347.219 345.406 348.156 361.062 350.031V331.891C361.062 309.297 346.859 298 318.453 298C303.266 298 287.703 300.344 271.766 305.031V292.375C287.703 287.688 303.266 285.344 318.453 285.344C356.703 285.344 375.828 300.625 375.828 331.188V433H366.828L363.453 418.375C344.984 428.125 327.078 433 309.734 433C275.516 433 258.406 419.078 258.406 391.234ZM316.906 359.875C287.75 359.875 273.172 370.188 273.172 390.812C273.172 410.5 285.359 420.344 309.734 420.344C327.734 420.344 344.844 415.562 361.062 406V362.688C345.406 360.812 330.688 359.875 316.906 359.875ZM527.844 428.781C515.656 431.594 502.531 433 488.469 433C438.781 433 413.938 407.453 413.938 356.359C413.938 309.016 438.781 285.344 488.469 285.344C502.531 285.344 515.656 286.75 527.844 289.562V302.219C514.719 299.406 502.062 298 489.875 298C450.031 298 430.109 317.453 430.109 356.359C430.109 399.016 450.031 420.344 489.875 420.344C502.062 420.344 514.719 418.938 527.844 416.125V428.781ZM561.875 261.438H572.281L574.953 285.344H619.25V298H576.219V391.234C576.219 410.641 583.344 420.344 597.594 420.344H619.25V433H597.875C573.875 433 561.875 419.734 561.875 393.203V261.438Z" fill="#169A9A"/>
<rect x="750" y="235.289" width="31.8247" height="230.476" fill="#169A9A"/>
<rect width="31.3672" height="303.406" transform="matrix(0.449366 0.893348 -0.910249 0.414062 1043.9 312.115)" fill="#169A9A"/>
<rect width="28.6454" height="308.952" transform="matrix(0.449366 0.893348 -0.910249 0.414062 1031.22 379.485)" fill="#169A9A"/>
<rect width="28.4584" height="161.512" transform="matrix(-0.575828 0.817571 -0.843444 -0.537217 918.051 322.056)" fill="#169A9A"/>
<rect width="27.5777" height="241.43" transform="matrix(-0.575828 0.817571 -0.843444 -0.537217 969.513 296.7)" fill="#169A9A"/>
</svg>
        '''.strip()
        self.package_json = '''
        
        '''