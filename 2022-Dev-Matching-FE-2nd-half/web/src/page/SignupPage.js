import ContentTitle from '../components/ContentTitle.js'

export default function SignupPage({ $target }) {
    this.$element = document.createElement('div');
    this.$element.id = 'form_container'

    new ContentTitle({ $target, title: 'Hello, GreatPeoPle!' });
    $target.appendChild(this.$element);

    this.render = () => {
        this.$element.innerHTML = `
            <span class="form_elem">
                <input id="name" placeholder="이름">
            </span>
            <span class="form_elem">
                <input id="email" placeholder="이메일">
            </span>
            <span class="form_elem">
                <select id="role" name="role">
                    <option value="">직군을 선택해주세요</option>
                    <option value="backend">백엔드</option>
                    <option value="frontend">프론트엔드</option>
                    <option value="fullstack">풀스택</option>
                </select>
            </span>
            <span class="form_elem">
                <button type="submit">등록</button>
            </span>
        `;
    };

    this.render();
};
