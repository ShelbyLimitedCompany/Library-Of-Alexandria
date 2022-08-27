import HomePage from '../page/HomePage.js'
import SignupPage from '../page/SignupPage.js'

export default function Header({ $target }) {

    this.$element = document.createElement('header');
    this.$page = document.createElement('main');

    $target.appendChild(this.$element);
    $target.appendChild(this.$page);

    const $router = () => {
        const routes = [
            { path: "/web/", view: HomePage },
            { path: "/web/signup", view: SignupPage },
        ]
    
        const pageMatches = routes.map((route) => {
            return {
                route,
                isMatch: route.path === location.pathname,
            };
        });

        let match = pageMatches.find((pageMatch) => pageMatch.isMatch);
    
        if (!match) {
            match = {
                route: location.pathname,
                isMatch: true,
            };
            new NotFound();
        } else {
            this.$page.innerHTML = '';
            new match.route.view({ $target: this.$page });
        }
    };

    document.addEventListener("DOMContentLoaded", () => {
        document.querySelector('header').addEventListener("click", (e) => {
            if (e.target.matches(".menu_name")) {
                e.preventDefault();
    
                const id = e.target.id.split('_')[1];
    
                if (id === 'home') {
                    history.pushState(null, null, '/web/');
                } else if (id === 'signup') {
                    history.pushState(null, null, '/web/signup');
                } else {
                    history.pushState(null, null, '/web/404');
                }
    
                $router();
            }
        });
        $router();
    });

    this.render = () => {
        this.$element.innerHTML = `
            <div class="header header_left">
                <span class="menu_name" id="menu_home">HOME</span>
            </div>
            <div class="header header_right">
                <div class="menu_name" id="menu_signup">SIGNUP</div>
            </div>
        `
    }

    window.addEventListener("popstate", () => {
        $router();
    });

    this.render();
};
