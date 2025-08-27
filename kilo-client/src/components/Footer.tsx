import "./styles/Footer.css"

function Footer() {
    return (
        <footer className="Footer">
            <div className="container">
                {/* CopyRight */}
                <p className="my-3">Kilo Access @ USF Powerlifting</p>

                {/* Mission Statement */}
                {/* <p className="small mb-4">
                    Welcome to the bright side of healthcare
                </p> */}

                {/* Links */}
                <div className="mb-5 mediaLinks">
                    {/* Github Link */}
                    <a
                        href="https://github.com/opey9519"
                        className="text-light mx-2 mediaLink"
                        aria-label="GitHub"
                    >
                        <i className="fab fa-github">
                            <img id="githubPhoto" src="/images/github-mark.png" alt="" />
                            GitHub
                            </i>
                    </a>
                    {/* LinkedIn Link */}
                    {/* <a
                        href="https://linkedin.com/in/gavin-wilson-ba6b67298/"
                        className="text-light mx-2 mediaLink"
                        aria-label="LinkedIn"
                    >
                        <i className="fab fa-linkedin">
                            <img id="linkedinPhoto" src="/images/LI-In-Bug.png" alt="" />
                            LinkedIn
                        </i>
                    </a> */}
                    {/* Dr Joonies Link */}
                    <a
                        href="https://www.instagram.com/powerliftingclubatusf/?hl=en"
                        className="text-light mx-2 mediaLink"
                        aria-label="USF_Powerlifting"
                        id="usfpowerliftingcontainer"
                    >
                        <i className="fab fa-joonies">
                            <img id="usfpowerlifting" src="/images/instagram_logo.png" alt="" />
                            Instagram
                        </i>
                    </a>
                </div>

                {/* Nav */}
                {/* <div className="navLinks">
                    <a href="/about" className="text-dark text-decoration-none mx-3 specLinks">
                        About
                    </a>
                    <a href="/privacy-policy" className="text-dark text-decoration-none mx-3 specLinks">
                        Privacy Policy
                    </a>
                    <a href="/terms-of-service" className="text-dark text-decoration-none mx-3 specLinks">
                        Terms of Service
                    </a>
                    <a href="/contact" className="text-dark text-decoration-none mx-3 specLinks">
                        Contact
                    </a>
                </div> */}

            </div>
        </footer>
    );
}

export default Footer;