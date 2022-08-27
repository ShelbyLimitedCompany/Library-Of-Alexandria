export default function ContentTitle({ $target, title }) {
    this.$element = document.createElement('div');
    this.$element.classList.add('content_title');

    $target.appendChild(this.$element);

    this.render = () => {
        this.$element.innerHTML = `<h1> ${title} </h1>`;
    };

    this.render();
};
