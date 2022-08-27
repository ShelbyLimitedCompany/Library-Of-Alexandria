import ContentTitle from '../components/ContentTitle.js'

export default function HomePage({ $target }) {
    this.$element = document.createElement('div');
    this.$element.id = 'cards_container'

    new ContentTitle({ $target, title: 'CardView' });
    $target.appendChild(this.$element);

    this.state = { people: localStorage.getItem('personalInfo')};

    const fetchPersonalInfos = new Promise((resolve, reject) => {
        const stored = localStorage.getItem('personalInfo');

        if (stored) {
            const people = JSON.parse(stored);
            const statusData = localStorage.getItem('cardStatus');

            if (statusData) {
                resolve({ people, status: JSON.parse(statusData) });
            } else {
                resolve({ people, status: data.map((d, i) => ({ idx: i, status: 'card' })) });
            }
        } else {
            fetch('/web/src/data/new_data.json')
                .then(response => response.json())
                .then(data => {
                    localStorage.setItem('personalInfo', JSON.stringify(data));
                    
                    const status = data.map((d, i) => ({ status: 'card' }));
                    localStorage.setItem('cardStatus', JSON.stringify(status));

                    resolve({ people, status });
                });
        }
    });

    function onClickCard(e) {
        e.preventDefault();
        e.target.classList.toggle('is-flipped');
    }

    this.render = () => {
        Promise
            .resolve(fetchPersonalInfos)
            .then(({ people, status }) => {
                this.$element.innerHTML = people.map((p, i) => `
                    <div idx="${i}" class=${status[i].status} onclick="${onClickCard}">
                        <div class="card_plane card_plane--front">${p.nickname}</div>
                        <div class="card_plane card_plane--back">${p.mbti}</div>
                    </div>
                `).join('');
            });
    };

    this.render();
};
