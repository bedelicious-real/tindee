import { useState } from 'react';
import ActionBar from '../../components/ActionBar/ActionBar';
import NavBar from '../../components/NavBar/NavBar';
import UserCard from '../../components/UserCard/UserCard';

import './Swipe.css';

export default function Swipe() {
	const dummyCandidate = {
		'email': 'a@x.com',
		'first-name': 'First',
		'image-url': 'https://storage.googleapis.com/tindee/avatar/7f04ec92b8198cd9b36d8d9a6f343476.png',
		'last-name': 'Last',
		'organization': 'Corp Inc.',
		'status': 'Junior',
		'edu-level': 'High School',
		'description': 'Here is my description. Thank you so much'
	};

	const [candidates, setCandidates] = useState([dummyCandidate]);

	const removeTopCandidate = () => {
		setCandidates(oldCandidates => oldCandidates.slice(1));
	};

	return (
		<div class="user-card">
			<UserCard candidate={candidates.length > 0 ? candidates[0] : null} />
			<ActionBar 
				candidate={candidates.length > 0 ? candidates[0] : null}
				targetEmail={candidates.length > 0 ? candidates[0]['email'] : null}
				removeTopCandidate={removeTopCandidate}
			/>
			<NavBar/>
		</div>
	)
}