
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

    
# {{ cookiecutter.project_name }}

A brief description of what this project does and who it's for


## Demo

Insert gif or link to demo

  
## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform

  
## Installation 

Install my-project with npm

```bash 
  npm install my-project
  cd my-project
```
    
## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

  
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

  
## Running Tests

To run tests, run the following command

```bash
  npm run test
```

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

  
## Deployment

To deploy this project run

```bash
  npm run deploy
```

  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

  
## Documentation

[Documentation](https://linktodocumentation)

  
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## Appendix

Any additional information goes here

  
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

  
## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?

  
## Support

For support, email fake@fake.com or join our Slack channel.

  
## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

  
## Used By

This project is used by the following companies:

- Company 1
- Company 2

  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  
## Optimizations

What optimizations did you make in your code? E.g. refactors, performance improvements, accessibility

  
## Roadmap

- Additional browser support

- Add more integrations

  
## License

{% if cookiecutter.open_source_license == 'MIT license' %}
[MIT](https://choosealicense.com/licenses/mit/)
{% endif %}

  
## Authors

- [@{{ cookiecutter.author_name }}](https://www.github.com/{{ cookiecutter.author_name }})

  
## Feedback

If you have any feedback, please reach out to us at fake@fake.com

  
## Related

Here are some related projects

[Awesome README](https://github.com/matiassingers/awesome-readme)

  
## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2

  